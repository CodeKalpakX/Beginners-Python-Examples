#Letters

letters = (
	'a',
	'b',
	'c',
	'd',
	'e',
	'f',
	'g',
	'h',
	'i',
	'j',
	'k',
	'l',
	'm',
	'n',
	'o',
	'p',
	'q',
	'r',
	's',
	't',
	'u',
	'v',
	'w',
	'x',
	'y',
	'z'
)

#Morse letters

morse_letters = (

	'.-',
	'-...',
	'-.-.',
	'-..',
	'.',
	'..-.',
	'--.',
	'....',
	'..',
	'.---',
	'-.-',
	'.-..',
	'--',
	'-.',
	'---',
	'.--.',
	'--.-',
	'.-.',
	'...',
	'-',
	'..-',
	'...-',
	'.--',
	'-..-',
	'-.--',
	'--..'
)


def text_to_morse(phrase):
	'''This function will help us to translate text to morse code'''

	translated_phrase = ''

	for letter in phrase.lower():

		if letter in letters or letter == ' ':

			for i in range(26): #Notice that the letters tuple and morse_letters tuple have same lenght (26)

				if letter == letters[i]:
					translated_phrase += morse_letters[i] + '/' 
					break

				elif letter == ' ':
					translated_phrase += ' /'
					break

		else:

			translated_phrase += 'invalid_char/' #If the user's input contains an invalid char like spanish letter Ñ 

	return translated_phrase


def morse_letter_to_normal_letter(letter):

	translated_letter = ''

	if letter in morse_letters or letter == ' ':
		for i in range(26):
			if letter == morse_letters[i]:
				translated_letter = letters[i]  #In this function we just do basically the same we did in the text_to_morse function
				break							#But know we translate a morse letter to a normal letter

			elif letter == ' ':
				translated_letter = ' '
				break
	else:

		translated_letter = ' (invalid_char) '

	return translated_letter


def morse_to_text(phrase):
	letter = ''     
	translated_phrase = ''

	for char in phrase:
		if char != '/':   	#Notice that Python doesn't know that a morse letter it's a group of . and - That's why we separate letters with /
			letter += char  #We do that to can append the - and . chars to the letter variable

		elif char == '/': #And when whe find a / we know that there's the end of a letter
			translated_phrase += morse_letter_to_normal_letter(letter) #So we call our morse_letter_to_normal_letter function and append the returned value to our finall translation
			letter = '' #And of course we arease the letter variable's content to continue with the next translation

	return translated_phrase 


if __name__ == '__main__':
	print(text_to_morse('Hello World')) #The output will be ...././.-../.-../---/ /.--/---/.-./.-../-../
	print(text_to_morse('Colombia')) # The output will be -.-./---/.-../---/--/-.../../.-/
	print(morse_to_text('..-/-./../-/./-../ /.../-/.-/-/./.../ /---/..-./ /.-/--/./.-./../-.-./.-/')) #The output will be united sates of america

	