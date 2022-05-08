# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Adds a user called swe573 without password and without 
# creating a home directory.
RUN adduser --disabled-password --no-create-home swe573
# Creates new directories for static and media files. 
# Then chown changes of the ownership of the files in a recursive manner
# as the application group. Finally permissions are set to ensure that
# application owner has read write access. 
RUN mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R swe573:swe573 /vol && \
    chmod -R 755 /vol
COPY . /code/