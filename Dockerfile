FROM python:3.12-slim

# Create a non-root user
RUN useradd -ms /bin/bash appuser

# Set default environment
ENV APP_ENV=development

WORKDIR /app

COPY requirements.txt .
COPY .env.development ./
COPY .env.testing ./
COPY .env.production ./
RUN apt-get update && apt-get install -y jq && apt-get install -y curl && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

# Change ownership of the app directory
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

EXPOSE 8000

# Health check to ensure the app is running
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]