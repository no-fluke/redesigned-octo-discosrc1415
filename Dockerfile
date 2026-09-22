FROM python:3.12.9-slim-bookworm

# Set working directory
WORKDIR /app

# Install system dependencies (FFmpeg)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default CMD (Heroku overrides this per dyno via heroku.yml)
CMD python3 bot.py
