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

![image](https://github.com/user-attachments/assets/33ec3691-7464-4869-b810-a28cdfbce2e8)


```bash
# 3. Copy Key API fedault and paste it to your .env file
WEATHER_API=your_openweathermap_api_key
```

### 3️. Install nodejs if it is not available

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

### 5. Create CI workflow to automation build lastest image and push it to Docker Hub

```bash
# 1. Create a free account for docker hub
Go to this page https://app.docker.com/
Create a free account on it or connect it with github account for faster registration

# 2. Create repository 
Go to this page https://hub.docker.com/repositories
Create repository to store the image after build successful
Forx eample:
```
![image](https://github.com/user-attachments/assets/89883650-7d1c-49c5-ae18-9587f065da02)

```bash
# 3. Create personal access for authetication log in
Go to this page https://app.docker.com/settings/personal-access-tokens
```
![image](https://github.com/user-attachments/assets/78042bb2-e989-43b1-b962-0a19e748fc54)
```bash
# 4. Update CI to authetication and push image to that repo
```
![image](https://github.com/user-attachments/assets/c31985eb-8f47-4df9-9189-b70b68a85b65)
