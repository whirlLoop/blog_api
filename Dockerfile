# Pull base image
FROM python:3.8.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /blog_api

# Install dependencies
COPY Pipfile Pipfile.lock /blog_api/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /blog_api/
COPY ./scripts/postgres_healthcheck.py /usr/local/bin/postgres_healthcheck
RUN chmod u+x /usr/local/bin/postgres_healthcheck
# CMD postgres_healthcheck && python src/core/manage.py migrate && python src/core/manage.py runserver 0.0.0.0:8000
