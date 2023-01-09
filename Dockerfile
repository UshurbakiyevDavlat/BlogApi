# Pull base image
FROM python:3.10.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies

# If you use pipenv inside project
#COPY Pipfile Pipfile.lock /code/
#RUN pip install pipenv && pipenv install --system


# Copy project
COPY . /code/

# If you use venv and requirements.txt
RUN pip install -U pip setuptools \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache
