FROM python:3.9

# Set environment variables:
ENV DEBUG_COLORS=true \
  TERM=xterm-256color \
  COLORTERM=truecolor \
  SHELL=/bin/bash \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

# Copy .bashrc with colourised prompt:
COPY .bashrc /root/.bashrc

# Install cron and nano:
RUN apt-get update && apt-get -y install cron nano

# Copy crontab:
COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

# Install Poetry:
RUN pip install "poetry==$POETRY_VERSION"

# Copy app directory into container:
WORKDIR /app
COPY . /app

# Project initialization:
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi

# start cron in foreground:
CMD ["cron", "-f"]