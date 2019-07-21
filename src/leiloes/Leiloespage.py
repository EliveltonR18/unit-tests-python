from selenium import webdriver
from NovoLeilaoPage import NovoLeilaoPage

class LeiloesPage():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def visita(self):
        self.driver.get("http://localhost:8080/leiloes")
    
    def novo(self):
        self.driver.find_element_by_link_text('Novo Leilão').click()
        leilaoPage = NovoLeilaoPage(self.driver)

        return leilaoPage
        
    
        