import random

game = True

while game :

	a = random.randint(1,3)

	if a == 1 :
		b = 'ROCK'
	elif a == 2 :
		b = 'PAPER'
	elif a == 3 :
		b = 'SCISSOR'

	print('')
	c = input('ENTER YOUR CHOICE - ')

	if c == 'R' :
		d = 'ROCK'
		e = 1
	elif c == 'P' :
		d = 'PAPER'
		e = 2
	elif c == 'S' :
		d = 'SCISSOR'
		e = 3
		
	print('')
	print('ROCK !')
	print('PAPER !!')
	print('SCISSOR !!!')
	print('SHOOT !!!!')
	print('')
	print('YOU CHOSE ',d,', OPPONENT CHOSE ',b)
	print('')

	if a == 1 :
		if e == 1 :
			print('IT\'S A TIE !')
		elif e == 2 :
			print('YOU WIN !')
		elif e == 3 :
			print('YOU LOST !')
	elif a == 2 :
		if e == 1 :
			print('YOU LOST !')
		elif e == 2 :
			print('IT\'S A TIE !')
		elif e == 3 :
			print('YOU WIN !')
	elif a == 3 :
		if e == 1 :
			print('YOU WIN !')
		elif e == 2 :
			print('YOU LOST !')
		elif e == 3 :
			print('IT\'S A TIE !')


