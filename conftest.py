import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
import logging
from browsermobproxy import Server


def pytest_addoption(parser):
    parser.addoption(
        "--b",
        action="store",
        default="chrome",
        help="Chose your browser"
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://localhost",
        help="Insert yout URL"
    )
    parser.addoption(
        "--path",
        action="store",
        default="/",
        help="Url path"
    )


@pytest.fixture(scope="session")
def browser(request):
    param = request.config.getoption("--b")
    if param == "chrome":
        wd = EventFiringWebDriver(webdriver.Chrome(), logger_listener())
        logging.info("CHROME SELECTED")
    elif param == "firefox":
        logging.info("FIREFOX SELECTED")
        opt = Options()
        opt.log.level="trace"
        wd = EventFiringWebDriver(webdriver.Firefox(options=opt), logger_listener()
        )
    else:
        logging.info("WRONG")
        raise ("Browser is not supported")
    wd.implicitly_wait(5)
    wd.get(request.config.getoption("--url") + request.config.getoption("--path"))
    request.addfinalizer(wd.quit)
    return wd



## -------------------logging part------------------- ##


logging.getLogger('test')
logging.basicConfig(filename='test.log', level=logging.DEBUG)


class logger_listener(AbstractEventListener):
    

    def before_find(self, by, value, driver):
        logging.info(msg=(by, value))

    def on_exception(self, exception, driver):
        logging.error(exception)
    
    def after_click(self, element, driver):
        logging.info("el clicked successfully")

    def after_find(self, by, value, driver):
        logging.info(by + " founded")

    def on_exception(self, exception, driver):
        logging.error(exception)

    def before_quit(self, driver):
        logging.info("test is done")