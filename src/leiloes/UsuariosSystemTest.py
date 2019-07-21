import unittest
from selenium import webdriver
from UsuariosPage import UsuariosPage

class SearchText(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/elive/Desktop/cesar-selenium/chromedriver")

    def testUser(self):
        usuario = UsuariosPage(self.driver)
        usuario.visita()
        usuario.novo().cadastra('Elivelton Rodrigues de Lima', 'elivelton.lima@seedabit.org')
        
        pageContent = self.driver.page_source

        self.assertIn('Elivelton Rodrigues de Lima', pageContent)
        self.assertIn('elivelton.lima@seedabit.org', pageContent)
    
    def testUserNameInvalid(self):
        usuario = UsuariosPage(self.driver)
        usuario.visita()
        usuario.novo().cadastraEmail('elivelton.lima@seedabit.org')
        
        pageContent = self.driver.page_source

        self.assertIn('Nome obrigatorio!', pageContent)

    def testUserEmailInvalid(self):
        usuario = UsuariosPage(self.driver)
        usuario.visita()
        usuario.novo().cadastraNulo()
        
        pageContent = self.driver.page_source
        self.assertIn('Nome obrigatorio!', pageContent)
        self.assertIn('E-mail obrigatorio!', pageContent) 

    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

