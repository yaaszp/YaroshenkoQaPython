import pytest


class TestVariables:
    CURRENT_URL = "https://rozetka.com.ua/ua/"
    ERROR_MESSAGE = "Необхідно підтвердити, що ви не робот"
    COUNT_PRODUCT = "1"


# Check that main elements of HomePage is visible
@pytest.mark.ui_additional
def test_homepage_is_visible(home_page):
    home_page.go_to()
    assert home_page.header_is_visible()
    assert home_page.sidebar_is_visible()
    assert home_page.main_content_is_visible()


# Check that current URL of HomePage is correct
@pytest.mark.ui_additional
def test_check_currenet_url(home_page):
    home_page.go_to()
    assert home_page.get_current_url() == TestVariables().CURRENT_URL


# Enter query in search field and check that url contain query word
@pytest.mark.ui_additional
def test_check_entering_query(home_page):
    home_page.go_to()
    home_page.enter_search_query("smartphone")
    # Check that URL contains query word
    assert home_page.analyze_current_url("smartphone")


# Check that login modal window is visible
@pytest.mark.ui_additional
def test_log_in_window_is_visible(home_page):
    home_page.go_to()
    home_page.click_log_in_button()
    assert home_page.log_in_window_is_visible()


# Check that cart modal window is visible
@pytest.mark.ui_additional
def test_cart_window_is_visible(home_page):
    home_page.go_to()
    home_page.click_cart_button()
    assert home_page.cart_window_is_visible()


# Check error message on modal log in window
@pytest.mark.ui_additional
def test_check_login_page(home_page):
    home_page.go_to()
    home_page.click_log_in_button()
    home_page.enter_email("test@gmail.com")
    home_page.enter_password("qwerty")
    home_page.click_remember_me_checkbox()
    home_page.click_enter_button()
    assert home_page.get_error_message() == TestVariables.ERROR_MESSAGE


# Add product to cart and check that count equal expected count
@pytest.mark.ui_additional
def test_check_count_product_in_cart(home_page):
    home_page.go_to()
    home_page.enter_search_query("smartphone")
    search_page = home_page.go_to_search_page()
    search_page.add_product_to_cart()
    assert search_page.get_count_product_from_cart() == TestVariables.COUNT_PRODUCT
