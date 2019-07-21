from selenium import webdriver
from NovoUsuarioPage import NovoUsuarioPage

class UsuariosPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def visita(self):
        self.driver.get("http://localhost:8080/usuarios")
    
    def novo(self):
        self.driver.find_element_by_link_text('Novo Usuário').click()
        usuarioPage = NovoUsuarioPage(self.driver)
        return usuarioPage
    
        