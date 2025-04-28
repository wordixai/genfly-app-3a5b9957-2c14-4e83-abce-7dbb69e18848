# Real Estate Management System with Streamlit Data Visualization

This project combines a Next.js frontend, Express.js API server, and Streamlit data visualization dashboard to provide comprehensive property management capabilities.

## Project Structure

- `src/` - Next.js frontend application
- `server/` - Express.js API server
- `streamlit_app/` - Streamlit data visualization dashboard

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.8+
- Docker and Docker Compose (optional)

### Environment Setup

1. Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql://username:password@localhost:5432/real_estate_db
```

2. Create a `.env` file in the `streamlit_app` directory:

```
API_BASE_URL=http://localhost:4000/api
```

### Running the Application

#### Without Docker

1. Start the Express server:

```bash
cd server
npm install
npm run dev
```

2. Start the Next.js application:

```bash
npm install
npm run dev
```

3. Start the Streamlit application:

```bash
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

#### With Docker

```bash
docker-compose up
```

## Accessing the Applications

- Next.js Frontend: http://localhost:8080
- Express API: http://localhost:4000
- Streamlit Dashboard: http://localhost:8501

## Features

- Property management
- Tenant tracking
- Financial analytics
- Maintenance scheduling
- Occupancy monitoring
- Interactive data visualizations