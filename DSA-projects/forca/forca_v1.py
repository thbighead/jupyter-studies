# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.hidden_word = '_' * len(word)
		self.board_status = 0
		self.wrong_letters = []

	# Método para adivinhar a letra
	def guess(self, letter):
		while letter in self.hidden_word or letter in self.wrong_letters:
			letter = input("Essa letra já foi escolhida, por favor tente outra: ")

		if letter in self.word:
			aux = list(self.hidden_word)
			for pos, char in enumerate(self.word):
				if char == letter:
					aux[pos] = letter
					self.hidden_word = ''.join(aux)
			del aux
		else:
			self.wrong_letters.append(letter)
			self.board_status += 1


	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.board_status >= len(board)-1 or self.word == self.hidden_word

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		return self.word == self.hidden_word

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[self.board_status])
		print(self.hidden_word, 'faltam', str(self.hidden_word.count('_')), 'letras.')
		print('Tentativas erradas: ', ', '.join(self.wrong_letters))


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
	return bank[random.randint(0,len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():
	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while(not game.hangman_over()):
		# Verifica o status do jogo
		game.print_game_status()
		game.guess(input("Tente uma letra: "))

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)

	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
	main()
