from selenium.webdriver.common.by import By

class CarrinhoPage:
    def __init__(self, driver):
        self.driver = driver

    #NÃO ESTÁ EM BOAS PRÁTICAS (NAO USAR ASSERT DENTRO DE CLASSES QUE NÃO SEJAM DE TESTES)
    def validar_produto_no_carrinho(self, nome_produto):
        itens = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        nomes = [item.text for item in itens]
        assert nome_produto in nomes

    def validar_produto_no_carrinho_correto(self, nome_produto):
        itens = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in itens]