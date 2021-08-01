word = input('ENTER A WORD TO GUESS - ')
	
def GAME(word) :

	length = len(word)
	characters = list(word)
	board = list('_'*length)
	print(board)

	a = True
	attempts = int(input('ATTEMPTS - '))

	while a :
		
		print('')
		print('YOU HAVE ' , attempts , ' ATTEMPTS LEFT')
		print('')
		guess = input('ENTER A LETTER - ')
		print('')

		for i , j in enumerate(characters) :
			if j == guess :
				board[i] = j
				print(board)
				print('')
		
		if guess not in word :
			attempts -= 1
			print(board)
			print('')
			
		if board == characters :
			print('YOU WIN !')
			print('THE ANSWER IS - ' , word)
			a = False	

		if attempts == 0 :
			print('YOU LOST !')
			print('THE ANSWER IS - ' , word)
			a = False

GAME(word)