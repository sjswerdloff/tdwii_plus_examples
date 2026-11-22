# Dockerfile of the project host image, with the tdwii_plus_examples package installed from the repository source.

FROM python:3.12.16-slim

# Copy the required project files from the repository root.
COPY pyproject.toml README.md /src/
COPY tdwii_plus_examples /src/tdwii_plus_examples

# Install the project and its dependencies, without keeping the download cache.
RUN pip install --no-cache-dir --root-user-action=ignore /src

# Keep the host running. The apps are started with docker compose exec.
CMD ["sleep", "infinity"]
