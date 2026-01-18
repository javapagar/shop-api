FROM python:3.13-slim

# Install uv from astral
# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh
# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Disable development dependencies
ENV UV_NO_DEV=1

WORKDIR /app

RUN mkdir ./data

COPY .env .
COPY .python-version .
COPY pyproject.toml .
COPY uv.lock .
COPY ./api ./api
COPY ./src ./src
COPY main.py .
RUN uv sync --locked

EXPOSE 8080

CMD [ "uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080",  "--workers", "4"]