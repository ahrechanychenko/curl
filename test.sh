echo 0. Build our build environment and produce image with standalone executable:
docker build -f build/Dockerfile build -t curl-static

echo 1. Turn on test environment
docker-compose up -d

pip3 install pytest lxml BeautifulSoup4
python3 -m pytest -v tests