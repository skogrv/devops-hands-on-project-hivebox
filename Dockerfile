FROM python:3.13
RUN adduser --disabled-login --shell /usr/sbin/nologin appuser \
    && mkdir -p /usr/local/app \
    && chown -R appuser:appuser /usr/local/app
USER appuser
WORKDIR /usr/local/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser src/ .
CMD ["python3", "main.py"]