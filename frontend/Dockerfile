# --- Stage 1: Build React frontend ---
FROM node:18 AS builder

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# --- Stage 2: Serve with NGINX ---
FROM nginx:stable-alpine

# Xóa cấu hình mặc định
RUN rm -rf /usr/share/nginx/html/*

# Copy build từ stage trước
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy cấu hình nginx nếu có
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]