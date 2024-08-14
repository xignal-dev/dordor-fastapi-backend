FROM python:3.11
RUN python -m pip install --upgrade pip
WORKDIR /fastapi
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt