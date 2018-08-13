#import json
def getShortQuotes(quotes, maxlen):
	'''
	Shortcut method to get the shorter quotes, need to convert to a better way of scrolling automatically	
	'''
	keys = quotes.keys()
	new_quotes = {}
	for key in keys:
		quote = quotes[key]
		if len(quote) < maxlen:
			new_quotes[key] = quote
	return new_quotes
	
def convertToDisplay(quote, wordLim):
	words = quote.split(' ')
	totLen = 0
	sentence = ''
	sentences = []
	for word in words:
		wordLen = len(word)+1
		totLen = totLen + wordLen
		sentence = sentence + ' ' + word
		if totLen > wordLim:
			sentences.append(sentence[0:totLen-len(word)])
			sentence  = ''+word
			totLen = len(word)
	if len(sentences) == 4:
		sentences[3] = sentences[3] + ' ' + word
	else:
		sentences.append(''+str(word)) 
	return sentences
			