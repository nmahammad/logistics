FROM python:3.12.1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# COPY django.sh /app/django.sh
# RUN chmod +x /app/django.sh

# ENTRYPOINT ["/app/django.sh"]
