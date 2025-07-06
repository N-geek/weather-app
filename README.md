# 🌤️ Weather Information App

http://k8s-default-weatherf-e138165e28-dc680244ba4d34b4.elb.us-east-1.amazonaws.com/

## ⚙️ Features

- 🔁 Get current weather data via street or city name
- 📦 Backend with FastAPI
- 💻 Frontend with React + Vite
- 🐳 Docker + Helm + K8s
- ☁️ AWS (EC2 + EKS + IAM + VPC)
- ✅ CI/CD with GitHub Actions
- 🔐 Prometheus + Grafana

---

## 🚀 Quick Start

### 1️. Clone the Repo

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2️. Get weather information
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

### 5. Weather application Result
http://k8s-default-weatherf-e138165e28-dc680244ba4d34b4.elb.us-east-1.amazonaws.com/

![image](https://github.com/user-attachments/assets/86df2aec-1ab0-444a-8390-545e7bd90656)

API website

http://k8s-default-weatherb-bb74c8ea9e-ed149abdef235d52.elb.us-east-1.amazonaws.com:5000/weather?query=London
{
  "location": "London, Greater London, Anh, Vương quốc Anh",
  "temp": 23,
  "description": "few clouds",
  "icon": "☁️"
}

![image](https://github.com/user-attachments/assets/1c8524cb-02a3-4a2f-b0e5-edfd0a89a8ce)

Prometheus
kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090
http://localhost:9090/

![image](https://github.com/user-attachments/assets/8c634bb9-c420-4687-8ab8-495f9dde84e1)


Grafana
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80
http://localhost:3000/

![image](https://github.com/user-attachments/assets/ee2f7e0a-8f27-4931-85d7-cd0619a0c8cf)


