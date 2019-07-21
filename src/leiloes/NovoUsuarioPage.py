from selenium import webdriver

class NovoUsuarioPage():

    def __init__(self, driver):
        self.driver = driver
    
    def cadastra(self, nome, email):
        self.name_input = self.driver.find_element_by_name('usuario.nome')
        self.email_input = self.driver.find_element_by_name('usuario.email')
        self.btnSalvar_input = self.driver.find_element_by_id('btnSalvar')

        self.name_input.send_keys(nome)
        self.email_input.send_keys(email)
        self.btnSalvar_input.click()

    def cadastraEmail(self, email):
        self.email_input = self.driver.find_element_by_name('usuario.email')
        self.btnSalvar_input = self.driver.find_element_by_id('btnSalvar')

        self.email_input.send_keys(email)
        self.btnSalvar_input.click()

    def cadastraNulo(self):
        self.btnSalvar_input = self.driver.find_element_by_id('btnSalvar')
        self.btnSalvar_input.click()
    
