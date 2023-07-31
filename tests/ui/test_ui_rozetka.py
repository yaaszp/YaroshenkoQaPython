import pytest
from modules.ui.page_objects.Rozetka.home_page import HomePage
from modules.ui.page_objects.Rozetka.log_in_page import LogInPage


@pytest.mark.ui_additional
def test_check_currenet_url():
    home_page = HomePage()
    home_page.go_to()
    assert home_page.get_current_url() == "https://rozetka.com.ua/ua/"
    home_page.close()


@pytest.mark.ui_additional
def test_check_entering_query():
    home_page = HomePage()
    home_page.go_to()
    home_page.enter_search_query("smartphone")
    assert home_page.get_current_url().count != 0
    home_page.close()


@pytest.mark.ui_additional
def test_homepage_is_visible():
    home_page = HomePage()
    home_page.go_to()
    assert home_page.header_is_visible() == True
    assert home_page.sidebar_is_visible() == True
    assert home_page.main_content_is_visible() == True
    home_page.close()


@pytest.mark.ui_additional
def test_log_in_window_is_visible():
    home_page = HomePage()
    home_page.go_to()
    home_page.click_log_in_button()
    assert home_page.log_in_window_is_visible() == True


@pytest.mark.ui_additional
def test_cart_window_is_visible():
    home_page = HomePage()
    home_page.go_to()
    home_page.click_cart_button()
    assert home_page.cart_window_is_visible() == True
