from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CarrinhoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #NÃO ESTÁ EM BOAS PRÁTICAS (NAO USAR ASSERT DENTRO DE CLASSES QUE NÃO SEJAM DE TESTES)
    def validar_produto_no_carrinho(self, nome_produto):
        itens = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        nomes = [item.text for item in itens]
        assert nome_produto in nomes

    def validar_produto_no_carrinho_correto(self, nome_produto):
        itens = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
        return [item.text for item in itens]
        #itens = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        #return [item.text for item in itens]