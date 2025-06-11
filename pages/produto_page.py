from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProdutoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def adicionar_produto_ao_carrinho(self, nome_produto):
        add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{nome_produto}']/ancestor::div[@class='inventory_item']//button")))
        add_btn.click()
        #self.driver.find_element(By.XPATH, f"//div[text()='{nome_produto}']/ancestor::div[@class='inventory_item']//button").click()
        
    # NÃO É BOAS PRATICAS TAMBÉM
    def verificar_produto_adicionado(self):
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.is_displayed()
        assert badge.text == '1', f'O número encontrado foi {badge.text}'

    def verificar_produto_adicionado_assert_na_classe_test(self):
        add_prod = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        return add_prod
        #return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    def acessar_carrinho(self):
        badge_btn = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        badge_btn.click()
        #self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()