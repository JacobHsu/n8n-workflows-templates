# Vercel 部署指南 / Vercel Deployment Guide

## 中文

### 準備工作
1. 確保您的專案已經推送到 GitHub 儲存庫
2. 在 [Vercel](https://vercel.com) 註冊帳號
3. 安裝 Vercel CLI（可選）：`npm i -g vercel`

### 部署步驟
1. **連接 GitHub**：在 Vercel 儀表板中連接您的 GitHub 帳號
2. **匯入專案**：選擇您的 n8n-workflows-templates 儲存庫
3. **配置設定**：
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: 留空
   - Install Command: 留空（Vercel 會自動處理 Python 依賴）

### 環境變數（可選）
在 Vercel 專案設定中添加：
- `PYTHON_VERSION=3.9`

### 注意事項
- 使用 **Python/FastAPI** 版本（`python run.py`）
- SQLite 資料庫會在每次部署時重新建立
- 工作流程索引會在建置時執行
- 所有 API 路由都會正常工作
- 多語言支援（繁體中文/英文）會正常運作

## English

### Prerequisites
1. Ensure your project is pushed to a GitHub repository
2. Sign up for a [Vercel](https://vercel.com) account
3. Install Vercel CLI (optional): `npm i -g vercel`

### Deployment Steps
1. **Connect GitHub**: Link your GitHub account in the Vercel dashboard
2. **Import Project**: Select your n8n-workflows-templates repository
3. **Configure Settings**:
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: leave empty
   - Install Command: leave empty (Vercel handles Python deps automatically)

### Environment Variables (Optional)
Add in Vercel project settings:
- `PYTHON_VERSION=3.9`

### Notes
- Uses **Python/FastAPI** version (`python run.py`)
- SQLite database will be recreated on each deployment
- Workflow indexing will run during build time
- All API routes will work normally
- Multi-language support (Traditional Chinese/English) will work

### Files Added for Vercel
- `vercel.json` - Vercel configuration for Python
- `api_server.py` - Modified FastAPI app with Vercel handler
- `requirements.txt` - Updated with mangum for ASGI adapter
- Multi-language files: `src/locales/zh-TW.json`, `src/locales/en.json`, `src/i18n.js`

### Project Structure
```
├── api_server.py          # Main FastAPI application
├── run.py                 # Local development launcher
├── workflow_db.py         # Database operations
├── vercel.json           # Vercel deployment config
├── requirements.txt      # Python dependencies
├── src/
│   ├── locales/         # Translation files
│   │   ├── zh-TW.json   # Traditional Chinese
│   │   └── en.json      # English
│   └── i18n.js          # Frontend i18n system
└── static/
    └── index.html       # Multi-language frontend
```