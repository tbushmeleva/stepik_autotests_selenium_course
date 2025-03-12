from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_make_parametrize_id(config, val): return repr(val)

# добавляем параметр запуска тестов language, по умолчанию выбирается en
def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose browser language (e.g., en, fr, de, ru, es)"
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language") # получаем параметр командной строки language

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    print("\nopen browser")

    yield browser
    print("\nquit browser..")
    browser.quit()
