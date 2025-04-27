FROM python:3.13
ENV FLASK_APP=src/app.py
RUN adduser --disabled-login --shell /usr/sbin/nologin appuser \
    && mkdir -p /usr/local/app \
    && chown -R appuser:appuser /usr/local/app
USER appuser
WORKDIR /usr/local/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser src/ src/
COPY --chown=appuser:appuser tests/ tests/
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]