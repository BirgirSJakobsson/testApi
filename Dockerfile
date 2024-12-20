# Stage 1: Base image
FROM python:3.12-slim AS base

# Set the working directory
WORKDIR /app

# Declare a volume for the SQLite database
# TODO:Change based on your environment
VOLUME /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Development stage
FROM base AS development
ENV APP_ENV=development

# Copy the environment file
COPY .env.development .env

# Install curl only in the development environment
RUN apt-get update && apt-get install -y curl sqlite3

# Copy application code
COPY . /app

# Create new User
RUN useradd -ms /bin/bash appuser

# Change ownership of the app directory
RUN chown -R appuser:appuser /app

# Switch to the new user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Set the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Stage 3: Testing stage
#FROM base AS testing
#ENV APP_ENV=testing
#COPY .env.testing .env
#COPY . /app

# Stage 4: Production stage
#FROM base AS production
#ENV APP_ENV=production
#COPY .env.production .env
#COPY . /app