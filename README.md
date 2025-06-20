# 🌤️ Weather Notification App

A fullstack weather application built with **FastAPI** (Python backend), **React** (frontend), **Tailwind CSS**, Docker, and GitHub Actions CI/CD. Weather data is fetched from [OpenWeatherMap](https://openweathermap.org/api).

## ⚙️ Features

- 🔁 Get current weather data via city name
- 📦 Backend with FastAPI
- 💻 Frontend with React + TailwindCSS
- 🐳 Dockerized with docker-compose
- ✅ CI/CD with GitHub Actions
- 🔐 Secrets managed via `.env`

---

## 🚀 Quick Start

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2️⃣ Clone the Repo
Create a .env file in both the root

```bash
WEATHER_API_KEY=your_openweathermap_api_key
```

### 3️⃣ Build & Run with Docker

```bash
docker-compose up --build
```

Visit frontend at: http://localhost:3000
Backend runs at: http://localhost:5000/weather?city=Hanoi
