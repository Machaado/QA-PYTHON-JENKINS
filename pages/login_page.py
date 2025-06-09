from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def preencherUsuario(self, usuario):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)

    def preencherSenha(self, senha):
        self.driver.find_element(By.ID, "password").send_keys(senha)

    def clicar_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    # NÃO DEVEMOS FAZER ASSERTS DENTRO DE CLASSES QUE NÃO SEJAM CLASSES DE TESTES, APENAS DEVEMOS RETORNAR OQUE QUEREMOS IGUAL EM (def verificarLoginS(self))
    def verificarLoginSucesso(self):
        assert "/inventory.html" in self.driver.current_url
        titulo = self.driver.find_element(By.CLASS_NAME, "title").text
        assert "Products" in titulo

    def verificarLoginS(self):
        return self.driver.find_element(By.CLASS_NAME, "title").text
    
    # NÃO É BOAS PRATICAS TAMBÉM
    def verificarLoginFalha(self):
        msg_error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").is_displayed()
        assert msg_error == True

    def verificarLoginFalhaCorreto(self):
        return self.driver.find_element(By.XPATH, "//h3[@data-test='error']")