import netifaces as ni
import os
import subprocess

import pytest

from bs4 import BeautifulSoup


@pytest.mark.functional
class TestWEB:
    @pytest.mark.https
    def test_https(self):
        print("\ngetting https site content")
        out = subprocess.run(['docker', 'run', '--rm',  '-t', 'curl-static', 'https://api.github.com'])
        assert out.returncode == 0

    @pytest.mark.unsecure_http
    def test_http(self):
        print("\ngetting http site content")
        ip = ni.ifaddresses('docker0')[ni.AF_INET][0]['addr']
        out = subprocess.run(['docker', 'run', '--rm', '-t', 'curl-static', 'http://{}:8080/test.html'.format(ip)],
                             stdout=subprocess.PIPE)
        print("checking that body contains 'curl curl curl'")
        assert "curl curl curl" in BeautifulSoup(out.stdout.decode('utf-8'), 'lxml').body.h1.text


@pytest.mark.ftp
class TestFTP:
    def test_curl_ftp_list(self):
        print("\ngetting ftp servel list of files")
        print("\nobtaining docker0 interface IP")
        ip = ni.ifaddresses('docker0')[ni.AF_INET][0]['addr']
        out = subprocess.run(['docker', 'run', '--rm', '-t', 'curl-static',
                              'ftp://test:test_pass@{}'.format(ip)],
                             stdout=subprocess.PIPE)
        assert "docker-compose.yml" in str(out.stdout)

    def test_curl_ftp_send(self):
        print("\nsending file via ftp")
        print("\nobtaining docker0 interface IP")
        ip = ni.ifaddresses('docker0')[ni.AF_INET][0]['addr']
        out = subprocess.run(['docker', 'run', '--rm',
                              '-v', '{}:/test'.format(os.getcwd()),
                              '-t', 'curl-static',
                              '-T', '/test/test_data/test_file.txt', 'ftp://test:test_pass@{}/test_file'.format(ip)])
        assert out.returncode == 0
        assert "test_file" in os.listdir()

    def test_curl_ftp_get(self):
        print("\nsending file via ftp")
        print("\nobtaining docker0 interface IP")
        ip = ni.ifaddresses('docker0')[ni.AF_INET][0]['addr']
        out = subprocess.run(['docker', 'run', '--rm',
                              '-v', '{}:/test'.format(os.getcwd()),
                              '-t', 'curl-static',
                              'ftp://test:test_pass@{}/test_file'.format(ip),
                             '-o', '/test/test_get'])
        assert out.returncode == 0
        assert "test_get" in os.listdir()
