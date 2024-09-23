# First Stage: Build dependencies
FROM python:3.12.5-slim-bookworm AS builder

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

# Set working directory
WORKDIR /app

# Install system dependencies for Poetry and FastAPI
RUN apt-get update && apt-get install -y curl build-essential

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy pyproject.toml and poetry.lock first to leverage Docker cache
COPY pyproject.toml poetry.lock /app/

# Install dependencies (no dev dependencies)
RUN poetry install --no-dev

# Copy the application code
COPY . /app

# Second Stage: Production Image
FROM python:3.12.5-slim-bookworm 

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app /app
COPY --from=builder /root/.local /root/.local

# Add Poetry to PATH in the final image
ENV PATH="/root/.local/bin:$PATH"

# Expose the port that FastAPI runs on
EXPOSE 8000

# Run the FastAPI application using Uvicorn
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
