#!/bin/bash

echo 0. Build our build environment and produce image with standalone executable:
docker build -f build/Dockerfile build -t curl-static

echo -e "\n"
echo 1 Run tests
pip3 install pytest lxml
python3 -m pytest -v tests