from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field

# 使用者註冊請求驗證
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="使用者名稱")
    email: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        description="電子郵件信箱"
    )
    password: str = Field(..., min_length=8, description="密碼 (最少 8 位字元)")
    role: Literal["consumer", "restaurant", "delivery_agent", "admin"] = Field(
        "consumer",
        description="帳戶角色"
    )

# 使用者登入請求驗證
class UserLogin(BaseModel):
    username: str = Field(..., description="使用者名稱")
    password: str = Field(..., description="密碼")

# 登入成功回傳的 Token
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# 使用者基本資訊回應 (不包含密碼雜湊)
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    created_at: datetime

    # Pydantic v2 ORM 模式設定
    model_config = ConfigDict(from_attributes=True)
