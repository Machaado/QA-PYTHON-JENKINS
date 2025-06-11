import pytest
from pages.login_page import LoginPage
import time

@pytest.mark.parametrize("usuario, senha", [
    ("standard_user", "secret_sauce")
])

def test_login_sucesso(driver, usuario, senha):
    login = LoginPage(driver)

    login.preencherUsuario(usuario)
    #time.sleep(2)
    login.preencherSenha(senha)
    #time.sleep(2)
    login.clicar_login()
    #time.sleep(2)
    #login.verificarLoginSucesso() NÃO DEVEMOS FAZER ASSERTS FORA DA CLASSE DE TESTE, DEVEMOS FAZER IGUAL ABAIXO, RECEBER O TEXTO DE UMA CLASSE EM UMA VARIAVEL, AQUI A VARIAVEL É msg
    #após isso, devemos fazer os asserts corretos
    msg = login.verificarLoginS()
    assert "/inventory.html" in driver.current_url
    assert "Products" in msg
    time.sleep(2)


@pytest.mark.parametrize("usuario, senha", [
    ("usuario_invalido", "senha_invalida")
])

def test_login_falha(driver, usuario, senha):
    login = LoginPage(driver)

    login.preencherUsuario(usuario)
    #time.sleep(2)
    login.preencherSenha(senha)
    #time.sleep(2)
    login.clicar_login()
    #time.sleep(2)
    login_falha = login.verificarLoginFalhaCorreto()
    assert login_falha.is_displayed()
    assert "not match" in login_falha.text
    #login.verificarLoginFalha()
    #time.sleep(2)