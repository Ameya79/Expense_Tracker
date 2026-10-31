# Multi-stage / lightweight production container for Expense Tracker
FROM python:3.12-slim

# Prevent Python from buffering stdout/stderr and writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

# Install runtime dependencies (curl for container healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create non-root user for security
RUN useradd -u 1000 -m appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

# Healthcheck to verify service responsiveness
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Production WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "app:app"]
