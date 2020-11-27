### three-letter-words.py ###


words = []
game = "play"

while game == "play":
	
	new = input("Enter a new 3 letter word: ")
	if len(new) != 3:
		print("That's not a 3-letter word")

	else:
			if new in words:
				#The user already entered this word.
				game = "over"
				print("You alread said that word. Game over.")
				print("You know " + str(len(words)) + " 3-letter words.")
				print(words)
			
			else:
				print("Nice one.")
				words.append(new)


