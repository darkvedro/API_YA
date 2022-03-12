import pytest

def pytest_addoption(parser):
    parser.addoption("--url",
                     default="https://ya.ru",
                     help="URL OFC")
    parser.addoption("--status_code",
                     action='store',
                     default=200,
                     help="KOD OTVETA",
                     type=int)

@pytest.fixture
def url_param(request):
    return request.config.getoption('--url')

@pytest.fixture
def status_code_param(request):
    return request.config.getoption('--status_code')