import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--b",
        action="store",
        default="firefox",
        help="Chose your browser"
    )
    parser.addoption(
        "--url",
        action="store",
        default="http://192.168.0.103",
        help="Insert yout URL"
    )
    parser.addoption(
        "--path",
        action="store",
        default="/",
        help="Url path"
    )


@pytest.fixture
def browser(request):
    param = request.config.getoption("--b")
    if param == "chrome":
        wd = webdriver.Chrome()
    elif param == "firefox":
        wd = webdriver.Firefox()
    else:
        raise ("Browser is not supported")
    wd.implicitly_wait(5)
    wd.get(request.config.getoption("--url") + request.config.getoption("--path"))
    return wd
