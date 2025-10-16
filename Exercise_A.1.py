import re
import string

file = "Taylor_Swift_Quotes.txt"

def clean(text):
    text = text.lower()                                                 #Lowercase
    text = re.sub(r'\d+', " ", text)                        #Remove digits
    text = text.translate(str.maketrans('', '', string.punctuation))    #Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()                #Remove überflüssige Leerzeichen
    return text

with open(file) as file:
    text = file.read()

cleaned_text = clean(text)

print(cleaned_text)

#store cleaned text in new file
with open('cleaned_text.txt', 'w') as file:
    file.write(cleaned_text)
