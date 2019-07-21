import unittest
from selenium import webdriver
from UsuariosPage import UsuariosPage
from Leiloespage import LeiloesPage
from NovoLeilaoPage import NovoLeilaoPage

class SearchText(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/elive/Desktop/cesar-selenium/chromedriver")
        usuario = UsuariosPage(self.driver)
        usuario.visita()
        usuario.novo().cadastra('Ellton Rodrigues', 'ellton@rodrigues.lima')
        
    def testUser(self):
        leilao = LeiloesPage(self.driver)
        leilao.visita()
        novoLeilao =  leilao.novo()
        novoLeilao.cadastra('Fogão', '124', 'Ellton Rodrigues', True)

        html = self.driver.page_source
        self.assertIn('Ellton Rodrigues', html)
        self.assertIn('Fogão', html) 
        self.assertIn('124.0', html) 
        self.assertIn('Sim', html) 

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

