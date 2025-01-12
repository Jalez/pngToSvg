#!/bin/bash
set -e

# Enable BuildKit for better caching
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1

echo "Building and running PNG to SVG converter..."
docker-compose build
docker-compose run --rm converter
echo "Conversion complete! Check output.svg"
