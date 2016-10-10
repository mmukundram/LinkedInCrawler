#sentence and work tokenizing

from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello Mr. Smith. How are you doing today? Isn't it a fine morning? Let's go for a jog."

print(sent_tokenize(text))
print(word_tokenize(text))


for i in word_tokenize(text):
	print i
