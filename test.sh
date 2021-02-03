#!/bin/bash
set -e

echo 0. Build our build environment and produce image with standalone executable:
docker build -f build/Dockerfile build -t curl-static

echo 1. Turn on test environment
docker-compose up -d

echo 2. Run tests
pip3 install pytest lxml BeautifulSoup4
python3 -m pytest -v tests

echo 3. Clean-up
docker-compose kill
docker-compose down

echo 4. Done
