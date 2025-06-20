# 🌤️ Weather Information App

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

### 1️. Clone the Repo

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2️. Clone the Repo
Create a .env file in both the root

```bash
# 1. How to get weather api
Go to https://home.openweathermap.org/users/sign_in and create a free account

# 2. Login
After login with free account > choose profile on the top right of the website > Chose My API keys
```

![image](https://github.com/user-attachments/assets/c1112b4f-7ccb-4f8e-9fba-0b248f507443)

```bash
# 3. Copy Key API fedault and paste it to your .env file
WEATHER_API=your_openweathermap_api_key
```

### 3️. Install nodejs if it is not available yet

```bash
# 1. Update your system
sudo apt update
sudo apt upgrade -y

# 2. Install curl if not installed
sudo apt install curl -y

# 3. Add NodeSource repo for latest Node.js (e.g., version 20)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -

# 4. Install Node.js and npm
sudo apt install -y nodejs

# 5. Verify installation
node -v
npm -v

# 6. npm install
cd frontend
npm install
```

### 4. Build & Run with Docker

```bash
docker-compose up --build
```

Visit frontend at: http://localhost:3000
![image](https://github.com/user-attachments/assets/c9509479-cde8-48f1-9a8c-a83220b0248d)

Backend runs at: http://localhost:5000/weather?city=Hanoi
![image](https://github.com/user-attachments/assets/371b20e4-cdd3-44a4-a843-5af96d77d111)

