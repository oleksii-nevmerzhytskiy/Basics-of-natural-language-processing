import spacy

my_file = open("input.txt", "r", encoding="UTF-8")
raw_text = my_file.read()
my_file.close()

nlp = spacy.load("en_core_web_sm")
text = nlp(raw_text)

output = ''
for word in text.ents:
    output += str(word.text + ' ' + word.label_ + "\n")
print(output)
my_file = open("output.txt", "w", encoding="UTF-8")
my_file.write(output)
my_file.close()
