import pytest
from modules.ui.page_objects.Rozetka.rozetka_home_page import HomePage
from modules.ui.page_objects.Rozetka.rozetka_log_in_page import LogInPage


# Check that main elements of HomePage is visible


@pytest.mark.ui_additional
def test_homepage_is_visible(home_page):
    home_page.go_to()
    assert home_page.header_is_visible() == True
    assert home_page.sidebar_is_visible() == True
    assert home_page.main_content_is_visible() == True
    home_page.close()


# Check that current URL of HomePage is correct


@pytest.mark.ui_additional
def test_check_currenet_url(home_page):
    home_page.go_to()
    assert home_page.get_current_url() == "https://rozetka.com.ua/ua/"
    home_page.close()


# Enter query in search field and check that url contain query word


@pytest.mark.ui_additional
def test_check_entering_query(home_page):
    home_page.go_to()
    home_page.enter_search_query("smartphone")
    assert home_page.get_text_from_url("smartphone") != 0
    home_page.close()


# Check that login modal window is visible


@pytest.mark.ui_additional
def test_log_in_window_is_visible(home_page):
    home_page.go_to()
    home_page.click_log_in_button()
    assert home_page.log_in_window_is_visible() == True


# Check that cart modal window is visible


@pytest.mark.ui_additional
def test_cart_window_is_visible(home_page):
    home_page.go_to()
    home_page.click_cart_button()
    assert home_page.cart_window_is_visible() == True


@pytest.mark.ui_additional
def test_check_login_page(home_page):
    login_page = home_page.go_to_login_page()
    # login_page.
    # login_page.
