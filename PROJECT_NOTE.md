# Project Note

## Thought Process
The goal was to build a simple yet functional stock market dashboard that demonstrates both backend and frontend skills, as well as an understanding of financial data. I started by outlining the required features and chose a tech stack that would allow for rapid development and easy integration: FastAPI for the backend (modern, async, and Pythonic), ReactJS for the frontend (responsive and interactive), and SQLite for lightweight data storage.

## Technologies Used
- **Backend:** FastAPI, SQLAlchemy, SQLite, Pandas
- **Frontend:** ReactJS, Chart.js (via react-chartjs-2), Axios
- **Containerization:** Docker, Docker Compose

## Implementation
I generated a mock CSV dataset with 10 companies and their historical stock prices. The backend loads this data into SQLite and exposes REST endpoints for companies, stock prices, and analytics (52-week high/low, average volume). The frontend fetches this data, displays a company list, and renders interactive charts and analytics. Loading spinners and error handling were added for a smooth user experience. The project is fully dockerized for easy deployment.

## Challenges Faced
The main challenge was ensuring seamless integration between the backend and frontend, especially with CORS and data formatting. Dockerizing both services and setting up a robust development workflow also required careful configuration. Overall, the project provided valuable experience in building and deploying a full-stack data-driven application. 