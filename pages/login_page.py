from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def preencherUsuario(self, usuario):
        user_field = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        user_field.clear()
        user_field.send_keys(usuario)
        #self.driver.find_element(By.ID, "user-name").send_keys(usuario)

    def preencherSenha(self, senha):
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(senha)
        #self.driver.find_element(By.ID, "password").send_keys(senha)

    def clicar_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()
        #self.driver.find_element(By.ID, "login-button").click()

    # NÃO DEVEMOS FAZER ASSERTS DENTRO DE CLASSES QUE NÃO SEJAM CLASSES DE TESTES, APENAS DEVEMOS RETORNAR OQUE QUEREMOS IGUAL EM (def verificarLoginS(self))
    def verificarLoginSucesso(self):
        assert "/inventory.html" in self.driver.current_url
        titulo = self.driver.find_element(By.CLASS_NAME, "title").text
        assert "Products" in titulo

    def verificarLoginS(self):
        title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return title.text
        #return self.driver.find_element(By.CLASS_NAME, "title").text
    
    # NÃO É BOAS PRATICAS TAMBÉM
    def verificarLoginFalha(self):
        msg_error = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").is_displayed()
        assert msg_error == True

    def verificarLoginFalhaCorreto(self):
        error_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        return error_msg
        #return self.driver.find_element(By.XPATH, "//h3[@data-test='error']")