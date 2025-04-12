FROM python:3.13
WORKDIR /usr/local/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src .
CMD ["python3", "main.py"]