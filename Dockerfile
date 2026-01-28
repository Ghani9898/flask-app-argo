FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies (this is RUN inside Dockerfile)
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
