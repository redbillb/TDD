from selenium import webdriver
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
		self.fail('Finish the test')

		# Ela é convidade a inserir um item de tarefa imediatamente

		# Ela digita "Buy peacock feathers" (Comprar penas de pavao) em uma caixa
		# de texto (o hobby de Edith é fazer iscawas para pesca com fly)

		# quando ela teclar enter, a pagina é atualizada, e agora a pagina lista
		# "1: Buy peacock feathers" como intem em uma lista de tarefas

		# Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
		# item. Ela insere "Use peacock feathers to make a fly" (usar penas de pavao
		# para fazer um fly - Edith é bem metodica)

		# A pagina é atualizada novamente e agora mostra os dois itens em sua lista

		# Edith se pergunta se o site lembrara de sua lista. Entao ela nota
		# que o site gerou um URL unico para ela -- ha um pequeno
		# texto explicativo para isso

		# ela acessa esse URL - sua lista de tarefas continua la.

		# satisfeita, ela volta a dormir
if __name__ == '__main__':
	unittest.main(warnings='ignore')
