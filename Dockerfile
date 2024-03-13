# Use Python 3.9 with Alpine Linux 3.13 as the base image
FROM python:3.9-alpine3.13

# Set metadata for the image
LABEL maintainer="londonappdeveloper.com"

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Copy requirements files and application code
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# Set working directory
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Set up Python virtual environment
RUN python -m venv /py

# Upgrade pip and install required system packages and Python packages
RUN /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache mysql-client mariadb-connector-c-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    /py/bin/pip install -r /tmp/requirements.dev.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# Add virtual environment's bin directory to PATH
ENV PATH="/py/bin:$PATH"

# Set the user for running the application
USER django-user
