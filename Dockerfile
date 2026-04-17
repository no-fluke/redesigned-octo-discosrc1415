FROM python:3.10.8-slim-bullseye

# Set working directory
WORKDIR /app

# Install system dependencies (FFmpeg)
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start application
CMD gunicorn app:app & python3 bot.py


# Rexbots
# Don't Remove Credit 🥺
# Telegram Channel @RexBots_Official
