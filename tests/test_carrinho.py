from pages.login_page import LoginPage
from pages.produto_page import ProdutoPage
from pages.carrinho_page import CarrinhoPage

import pytest
import time

@pytest.mark.parametrize("usuario, senha, nome_produto", [
    ("standard_user", "secret_sauce", "Sauce Labs Backpack")
])

def test_validar_produto_carrinho(driver, usuario, senha, nome_produto):
    """Deve logar, adicionar item ao carrinho, abrir o carrinho e verificar se o produto adicionado se encontra lá"""
    login = LoginPage(driver)
    produto = ProdutoPage(driver)
    carrinho = CarrinhoPage(driver)

    
    login.preencherUsuario(usuario)
    #time.sleep(1)
    login.preencherSenha(senha)
    #time.sleep(1)
    login.clicar_login()
    #time.sleep(1)
    

    
    produto.adicionar_produto_ao_carrinho(nome_produto)
    #time.sleep(1)

    badge = produto.verificar_produto_adicionado_assert_na_classe_test()
    assert badge.is_displayed()
    assert badge.text == '1', f'O número encontrado foi {badge.text}'
    
    #time.sleep(1)
    produto.acessar_carrinho()
    #time.sleep(1)
    

    
    nomes = carrinho.validar_produto_no_carrinho_correto(nome_produto)
    assert nome_produto in nomes

    #carrinho.validar_produto_no_carrinho(nome_produto)
    #time.sleep(1)
    ####