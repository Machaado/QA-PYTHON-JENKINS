from selenium.webdriver.common.by import By

class ProdutoPage:
    def __init__(self, driver):
        self.driver = driver

    def adicionar_produto_ao_carrinho(self, nome_produto):
        self.driver.find_element(By.XPATH, f"//div[text()='{nome_produto}']/ancestor::div[@class='inventory_item']//button").click()
        
    # NÃO É BOAS PRATICAS TAMBÉM
    def verificar_produto_adicionado(self):
        badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.is_displayed()
        assert badge.text == '1', f'O número encontrado foi {badge.text}'

    def verificar_produto_adicionado_assert_na_classe_test(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    def acessar_carrinho(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()