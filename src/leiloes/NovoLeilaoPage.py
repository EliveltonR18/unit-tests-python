from selenium import webdriver
from selenium.webdriver.support.ui import Select

class NovoLeilaoPage():

    def __init__(self, driver):
        self.driver = driver
    
    def cadastra(self, nome, valor, usuario, usado):
        self.txtNome = self.driver.find_element_by_name('leilao.nome')
        self.txtValor = self.driver.find_element_by_name('leilao.valorInicial')
        
        self.txtNome.send_keys(nome)
        self.txtValor.send_keys(valor)

        cbUsuario = Select(self.driver.find_element_by_name('leilao.usuario.id'))
        cbUsuario.select_by_visible_text(usuario)

        if usado :
            self.ckUsado = self.driver.find_element_by_name('leilao.usado')
            self.ckUsado.click()
        
        self.txtNome.submit()

