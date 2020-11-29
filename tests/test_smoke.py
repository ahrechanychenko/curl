import os
import subprocess
import pytest

@pytest.mark.smoke
class TestSmoke:
    def test_curl_version(self):
        print("Checking curl --version")
        out = subprocess.run(['docker', 'run', '--rm',  '-t', 'curl-static', '--version'])
        assert out.returncode == 0

    def test_curl_help(self):
        print("Checking curl --help")
        out = subprocess.run(['docker', 'run', '--rm',  '-t', 'curl-static', '--help'])
        assert out.returncode == 0

    def test_curl_empty(self):
        print("Checking curl without args")
        out = subprocess.run(['docker', 'run', '--rm',  '-t', 'curl-static'])
        assert out.returncode != 0
