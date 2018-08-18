from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith ouvio falar de uma nova aplicacao online interessante para
        # lista de tarefas. Ela decide verificarf sua homepage
        self.browser.get('http://localhost:8000')


        # Ela percebe que o titulo da pagina e o cabecalho mencionam listas de
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # Ela é convidade a inserir um item de tarefa imediatamente
        inputbox = self.browser.find.element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item')

        # Ela digita "Buy peacock feathers" (Comprar penas de pavao) em uma caixa
        # de texto (o hobby de Edith é fazer iscawas para pesca com fly)
        inputbox.send_keys('Buy peacock feathers')

        # quando ela teclar enter, a pagina é atualizada, e agora a pagina lista
        # "1: Buy peacock feathers" como intem em uma lista de tarefas
        inputbox.send_keys(keys.Enter)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
            )
        
        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # item. Ela insere "Use peacock feathers to make a fly" (usar penas de pavao
        # para fazer um fly - Edith é bem metodica)

        self.fail('Termine os testes!(Finish the tests)')

        # A pagina é atualizada novamente e agora mostra os dois itens em sua lista

        # Edith se pergunta se o site lembrara de sua lista. Entao ela nota
        # que o site gerou um URL unico para ela -- ha um pequeno
        # texto explicativo para isso

        # ela acessa esse URL - sua lista de tarefas continua la.

        # satisfeita, ela volta a dormir
if __name__ == '__main__':
    unittest.main(warnings='ignore')
