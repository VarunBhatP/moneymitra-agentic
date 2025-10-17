FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["gunicorn", "moneymitra.wsgi:application", "--bind", "0.0.0.0:8000"]
