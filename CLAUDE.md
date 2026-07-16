# Claude 開發規範引導 (Claude Code Guidelines)

本專案所有的開發規範、技術選型、憑證安全與 AI 協作原則皆已統一記錄於根目錄的 `AGENTS.md` 中。

請在開始進行任何開發與代碼修改前，閱讀並遵守該規範：
👉 [AGENTS.md](file:///c:/Users/poyi0/OneDrive/Desktop/delivery/AGENTS.md)

### 快速導覽
*   技術棧：React (前端) + FastAPI (後端)
*   資料庫：SQLite (開發) / Render PostgreSQL (正式)
*   安全核心：嚴禁硬編碼任何憑證或連線字串，必須使用環境變數與 `.env`，且 `.env` 必須被加入至 `.gitignore`。
