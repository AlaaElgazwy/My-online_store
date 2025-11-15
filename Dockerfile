FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app


RUN apt-get update && apt-get install -y build-essential libpq-dev gcc

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app


RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "ecommerce_project.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]
