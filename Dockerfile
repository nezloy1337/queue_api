FROM python:3.13-slim  AS base

#stage 1
# Update packages and install curl for downloading
RUN apt-get update \
  && apt-get install -y --no-install-recommends curl \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean


#stage 2
FROM base AS poetry-export

# Set environment variables for Poetry
ENV PATH=$PATH:/root/.local/bin \
    POETRY_VERSION=1.8.3

RUN curl -sSL https://install.python-poetry.org | python - --version $POETRY_VERSION
COPY pyproject.toml poetry.lock ./

# Export main dependencies to requirements.txt
RUN poetry export --no-interaction -o /requirements.txt --without-hashes --only main


#stage 3
FROM base AS requirements

RUN apt-get update && apt-get install -y gcc python3-dev --no-install-recommends && apt-get clean
COPY --from=poetry-export /requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


#stage 4
FROM base AS source
WORKDIR /app

# Copy application source code from the source stage
COPY fastapi_application /app/fastapi_application
COPY pyproject.toml /app
COPY README.md /app
COPY .env /app
COPY alembic.ini /app

#stage 5
FROM base AS final
WORKDIR /app

# Copy installed Python packages from the requirements stage
COPY --from=requirements /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=requirements /usr/local/bin /usr/local/bin

# Copy application source code from the source stage
COPY --from=source /app /app

# Set environment variables for the app
ENV PORT=8000 HOST=0.0.0.0
ENV PYTHONPATH=/app/fastapi_application

# Command to run the FastAPI application
CMD ["uvicorn", "fastapi_application.main:main_app", "--host", "0.0.0.0", "--port", "50000"]