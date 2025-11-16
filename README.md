# 🛒 E-Commerce Platform (Django + Docker + PostgreSQL)

A production-ready e-commerce web application built with **Django**, containerized using **Docker**, and powered by **PostgreSQL** and **Gunicorn** for deployment.  
This project includes user authentication, product management, and a basic API structure.

---

## 🚀 Features

- User Registration & Login  
- Product CRUD (Add / Update / Delete)  
   
- User Profile Page  
- Fully Dockerized Backend  
- PostgreSQL Database  
- Gunicorn Application Server  
- Environment-driven configuration  

---

## 🧰 Technologies Used

- **Django 5**
- **Python 3.12**
- **Docker & Docker Compose**
- **PostgreSQL**
- **Gunicorn**
- **Linux / Ubuntu**

---

## 📦 Project Structure

ecommerce_project/
│── ecommerce/ # Django project
│── store/ # Main app (Products / Categories)
│── users/ # Authentication & Profiles
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md


---

## Run with Docker

### 1️ Build Images
```bash
docker-compose build

### 2- Start Containers

docker-compose up -d

3️⃣ Apply Migrations

docker-compose exec web python manage.py migrate

4️⃣ Create Superuser

docker-compose exec web python manage.py createsuperuser

5- Open in Browser

Main Site: http://localhost:8000

Docker Hub Image

Repository:
https://hub.docker.com/r/alaaelgazwy/ecommerce

Upcoming Enhancements (Roadmap)

These will be added in the next phase:

✔️ Nginx Reverse Proxy

To serve static files & proxy requests to Gunicorn.

✔️ CI/CD using Jenkins

Automated build, test, and Docker deployment pipeline.

✔️ Kubernetes Deployment

Production orchestration using a multi-container setup.

✔️ Monitoring & Logging

Using Prometheus, Grafana, and Loki.

👨‍💻 Author

Alaa Elgazwy
DevOps Engineer
GitHub: https://github.com/alaaelgazwy
