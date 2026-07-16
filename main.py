from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import User
from .schemas import TokenResponse, UserLogin, UserRegister, UserResponse
from .security import create_access_token, hash_password, verify_password

# 於啟動時自動建立資料庫資料表 (適用於 SQLite 本地環境)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="餐廳外送系統 API", version="1.0.0")

# 設定跨來源資源共用 (CORS) 阻擋，防範前端存取安全性問題
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 正式環境應限制來源網域
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "餐廳外送系統 API 運作中"}

# 註冊 API
@app.post(
    "/api/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="使用者註冊"
)
def register_user(user_data: UserRegister, db: Session = Depends(get_db)):
    # 1. 檢查帳號是否重複
    existing_username = db.query(User).filter(User.username == user_data.username).first()
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="該使用者名稱已有人使用"
        )
    
    # 2. 檢查信箱是否重複
    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="該電子郵件信箱已有人註冊"
        )
    
    # 3. 密碼加密並儲存
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 登入 API
@app.post(
    "/api/auth/login",
    response_model=TokenResponse,
    summary="使用者登入並核發 Token"
)
def login_user(login_data: UserLogin, db: Session = Depends(get_db)):
    # 1. 根據帳號查詢使用者
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="使用者名稱或密碼錯誤",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 2. 核發 JWT Token，Payload 包含帳號與角色
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role}
    )
    return {"access_token": access_token, "token_type": "bearer"}
