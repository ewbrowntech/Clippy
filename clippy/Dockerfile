FROM python:3.11
WORKDIR /app

# Install Poetry for dependency management
RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy the rest of your application's code
COPY . /app

# Command to run the FastAPI app
CMD ["python", "app/bot.py"]