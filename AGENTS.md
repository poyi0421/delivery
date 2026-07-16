# AI 開發與協作規範 (AI Development & Collaboration Guidelines)

## 1. 專案概述與技術選型 (Project Overview & Tech Stack)
本專案為一個「餐廳外送系統」，旨在為學生與上班族群提供流暢的點餐與外送服務。開發與部署的技術規範如下：
*   **前端框架**：React SPA (採用響應式 RWD 設計，特別優化行動裝置體驗)
*   **後端框架**：FastAPI (Python)
*   **本地開發資料庫**：SQLite
*   **正式生產資料庫**：Render PostgreSQL
*   **部署平台**：Render.com (託管前端與後端服務)

## 2. 憑證與資安規範 (Security & Credential Management)
*   **嚴禁提交機密**：任何 API Key、密碼、Token（如 JWT Secret）、資料庫連線字串等敏感機密資訊，**絕對禁止**提交至 Git 版本控制系統，亦不得以任何形式硬編碼 (Hardcode) 於程式碼中。
*   **環境變數管理**：所有敏感配置與連線資訊均必須透過環境變數 (Environment Variables) 進行存取。
*   **本地環境配置**：
    *   在專案根目錄建立 `.env.example`，列出所有專案運行所需的環境變數名稱與說明的模擬預設值，但**嚴禁寫入真實憑證**。
    *   實際運作的 `.env` 檔案必須加入至 `.gitignore` 中，確保其不被 Git 追蹤與提交。

## 3. 開發與提交規範 (Development & Git Rules)
*   **程式碼品質**：後端程式碼需符合 PEP 8 規範，並使用 Pydantic 作為 API 資料校驗與過濾；前端應模組化元件，維持清晰的架構。
*   **資料庫變更**：任何資料庫 Schema 的修改，均須透過 Alembic 產生遷移指令腳本 (Migration Scripts)，不得手動直接修改正式資料庫。
*   **AI 協作規則**：
    *   AI 代理與開發者在開發新功能前，應優先讀取並遵循 `/doc/project-memory.md` 所記錄的決策，並更新 `/doc/todo.md` 中的任務狀態。
    *   任何新技術的選型或既有架構設計的重大變更，均須在 `/doc/project-memory.md` 記錄更新。
