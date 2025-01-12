#!/bin/bash

echo "Checking Docker image for dependencies..."

# Quick check if image exists
if ! docker images | grep -q pngtosvg-converter; then
    echo "❌ Docker image not built yet. Run ./convert.sh first"
    exit 1
fi

# Check potrace
echo -n "Checking potrace: "
if docker run --rm pngtosvg-converter which potrace >/dev/null 2>&1; then
    echo "✅ $(docker run --rm pngtosvg-converter potrace --version)"
else
    echo "❌ not found"
fi

echo "Done checking dependencies."
