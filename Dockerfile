FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app


RUN apt-get update && apt-get install -y build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --timeout 1000 -r requirements.txt

COPY . /app

# IMPORTANT: Collect static files into the STATIC_ROOT directory.
# This directory will be shared via the 'static_volume'.
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "ecommerce_project.wsgi:application", "--bind", "0.0.0.0:8000"]
