"""This script uses selenium to simulate shimo.im login"""
# Import system lib
import time
import sys
import pprint
# Import third party lib
import pretty_errors
from python_settings import settings
import settings as my_local_settings
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException


def sleep(_seconds: int):
    """Sleep decorator

    :param _seconds: Number of seconds to sleep
    :return: None
    """
    def the_real_decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            time.sleep(_seconds)
        return wrapper
    return the_real_decorator


def create_chrome_browser_and_login(_url: str) -> dict:
    """Create a chrome type browser

    :param _url: web url
    :return: Logged browser cookies in dict format
    """
    _cookies = {}
    try:
        _browser = webdriver.Chrome()
        _browser.get('https://shimo.im/login?from=home')
        # Get login credentials from settings.py and login
        settings.configure(my_local_settings)
        _email, _password = settings.USER_EMAIL, settings.USER_PASSWORD
        # Login to shimo
        login_shimo_by_email(_browser, _email, _password)
        _cookies = _browser.get_cookies()
    except Exception as e:
        sys.exit(f'[ERROR]: Failed creating chrome browser, {e}')
    finally:
        _browser.close()
    return _cookies


@sleep(10)
def login_shimo_by_email(_browser: webdriver.Chrome, _email: str, _password: str):
    """Log into shimo

    :param _browser: webdriver browser obj
    :param _email: Login email
    :param _password: Login password
    :return: webdriver Chrome browser obj
    """
    try:
        _browser.find_element_by_name('mobileOrEmail').send_keys(_email)
        _browser.find_element_by_name('password').send_keys(_password)
        _browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    except NoSuchElementException as e:
        sys.exit(f'[ERROR]: No element find, {e}')
    except ElementClickInterceptedException as e:
        sys.exit(f'[ERROR]: Click command could be completed, {e}')


if __name__ == '__main__':
    # Define url
    url = 'https://shimo.im/login?from=home'
    # Create browser and login
    cookies = create_chrome_browser_and_login(url)
    # Print cookies
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(cookies) if cookies else print(f'Something is wrong, empty cookies')
