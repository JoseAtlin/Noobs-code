import random

def start():
	f = open('dictionary.txt',mode='r')			
	length = int(input("Pick the size of word between \'4\' - \'10\' : "))
	attempts = int(input("Enter the no. of attempts needed : "))
	if attempts < length:
		print("Can you solve this?? {} < {} Good Luck".format(attempts,length).center(140))

	words = []
	for line in f:
		if len(line.strip()) == length:
			words.append(line.strip().lower())

	word = list(random.choice(words))
	user = ['_']*length
	print("\nComputer is selecting a {} letter word...\n".format(length))
	play(attempts,length,word,user)

def play(attempts,length,word,user):
	guess = []
	symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','/','`','~']
	while(1):
		count = 0
		while(attempts > 0):
			flag = 0
			print(("Word : "+' '.join(user)).center(140))
			print("Attempts Remaining : {}".format(attempts))
			if len(guess) == 0:
				print("Previous Guesses : NIL")
			else:
				print("Previous Guesses : {}".format(' '.join(guess)))

			letter = input("Choose a letter : ").lower()
			if len(letter) > 1:
				print("choose only a letter, No words".center(140,'-'))
				continue
			if letter.isdigit():
				print("Choose only a letter, No Numbers".center(140,'-'))
				continue
			if letter in symbols:
				print("Choose only a letter, No symbols".center(140,'-'))
				continue

			for i in range(len(word)):
				if word[i] == letter:
					user[i] = letter
					guess.append(letter)
					print("You guessed right..!\n".center(140))
					flag = 1
					count += 1
					break
			if flag == 0:
				guess.append(letter)
				print("Ooops.. {} is not in the word\n".format(letter).center(140))	

			if count == len(word):
				print("You've Won !! Great Job...".center(140,'-'))
				print('\n')
				break

			if attempts == 1:
				print("Ooops you are out of moves :(".center(140,'-'))
				print("Better luck next time\n".center(140))
				print("Word was : {}".format(''.join(word)).rjust(140))
			attempts -= 1

		print("Do you wish to play again?".center(140))
		print("1.Restart  2.End Game\n".center(140))
		ch = int(input("Enter your Choice : "))
		print('\n')
		if ch == 1:
			start()
		elif ch == 2:
			break

pattern = [('.|.'*(2*i + 1)).center(140,'-') for i in range(5//2)]
print('\n'.join(pattern + ['WELCOME TO HANGMAN'.center(140, '-')] + pattern[::-1]))
print('\n')

Name = input("Enter your Name : ")
print("{} is playing...".format(Name).rjust(140))
start()
