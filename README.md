# Stock Market Dashboard

A full-stack stock market dashboard application built with FastAPI (Python), ReactJS, and SQLite. The app allows users to browse companies, view historical stock price charts, and see key analytics like 52-week high/low and average volume.

## Features
- Responsive UI with sidebar company list and main chart area
- Interactive stock price chart (Chart.js)
- 52-week high/low and average volume analytics
- REST API backend (FastAPI, Python)
- SQLite database with mock stock data
- Dockerized for easy deployment

## Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Frontend:** ReactJS
- **Containerization:** Docker, Docker Compose

## Getting Started

### Prerequisites
- Docker & Docker Compose (recommended)
- Or: Python 3.11, Node.js, npm

### Local Development
#### Backend
```sh
cd backend
python -m venv venv
./venv/Scripts/activate  # On Windows
pip install -r requirements.txt
python load_data.py  # Load mock data
python -m uvicorn main:app --reload --port 8000
```
#### Frontend
```sh
cd frontend
npm install
npm start
```

### Docker (Recommended)
From the project root:
```sh
docker-compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

## API Endpoints
- `GET /companies` — List all companies
- `GET /stocks/{company_id}` — Historical prices for a company
- `GET /analytics/{company_id}` — 52-week high/low, average volume

## Deployment
- Deploy easily to Render, Railway, or any Docker-compatible cloud
- For static frontend, you can use Vercel/Netlify (after building React app)

## Sample Data
- See `backend/mock_stock_data.csv` for the sample dataset

## Screenshots
<img width="940" height="443" alt="image" src="https://github.com/user-attachments/assets/75916c6b-397d-4287-92ca-614808cbc037" />

<img width="940" height="444" alt="image" src="https://github.com/user-attachments/assets/d248955a-a2e6-4292-8a8f-d24f178f7380" />

<img width="940" height="446" alt="image" src="https://github.com/user-attachments/assets/049ee96e-d887-479e-8587-b95c8703ba59" />

<img width="940" height="446" alt="image" src="https://github.com/user-attachments/assets/53e344b4-28b7-4846-b2a1-79e9a200e447" />


## License
MIT 
=======
# stock-market-dashboard
>>>>>
