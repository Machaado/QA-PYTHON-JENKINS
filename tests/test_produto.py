from pages.login_page import LoginPage
from pages.produto_page import ProdutoPage

import pytest
import time

@pytest.mark.parametrize("usuario, senha, nome_produto", [
    ("standard_user", "secret_sauce", "Sauce Labs Backpack")
])

def test_adicionar_produto(driver, usuario, senha, nome_produto):
    """Deve permitir que adicione itens ao carrinho e verificar se apareceu a notificação de 1 item adicionado ao carrinho"""
    login = LoginPage(driver)
    produto = ProdutoPage(driver)

    login.preencherUsuario(usuario)
    #time.sleep(1)
    login.preencherSenha(senha)
    #time.sleep(1)
    login.clicar_login()
    #time.sleep(1)

    produto.adicionar_produto_ao_carrinho(nome_produto)
    #time.sleep(1)
    #produto.verificar_produto_adicionado()
    #time.sleep(1)
    badge = produto.verificar_produto_adicionado_assert_na_classe_test()
    assert badge.is_displayed()
    assert badge.text == '1', f'O número encontrado foi {badge.text}'
    #time.sleep(1)