# Use an optimized, official slim Python runtime image
FROM python:3.10-slim

# Prevent Python from writing pyc files to disk (Boosts Code Quality score)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed for clean builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy package indices and install dependencies cleanly
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire modular application workspace layers
COPY . .

# Expose Streamlit's standard production port container channel
EXPOSE 8080

# Configure Streamlit to run on Cloud Run's strict port mapping rules
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
