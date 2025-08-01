FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire Django project
COPY . .

# Run Django with gunicorn
CMD ["gunicorn", "beaunity.wsgi:application", "--bind", "0.0.0.0:8000"]

# Create a user and group (e.g., 'django') with non-root privileges
RUN groupadd -r django && useradd -r -g django django

# Change ownership of app files to django user
RUN chown -R django:django /app

# Switch to the non-root user
USER django
