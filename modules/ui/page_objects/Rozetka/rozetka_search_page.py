from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from modules.ui.page_objects.Rozetka.rozetka_base_page import BasePage


class SearchPage(BasePage):
    ADD_TO_CART_BUTTON = "//rz-search/rz-catalog//section/rz-grid/ul/li[2]/rz-catalog-tile/app-goods-tile-default//app-buy-button/button"
    CART_BUTTON = "//rz-header/rz-main-header/header//rz-cart/button"
    COUNT_PRODUCT_IN_CART = "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[7]/rz-cart/button/rz-icon-badge/span"

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def add_product_to_cart(self):
        wait = WebDriverWait(self.driver, timeout=15)
        add_to_cart = wait.until(
            lambda d: d.find_element(By.XPATH, self.ADD_TO_CART_BUTTON)
        )
        add_to_cart.click()

    def get_count_product_from_cart(self):
        element = self.driver.find_element(By.XPATH, self.COUNT_PRODUCT_IN_CART)
        return element.text
