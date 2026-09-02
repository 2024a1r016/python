#take a sentence containing double spaces and unwanted spaces in the beginning or end.Clean the sentence
word=input(" ")
word=word.strip()
word=word.replace("  "," ")
print(word)