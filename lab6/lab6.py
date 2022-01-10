from transformers import MarianTokenizer, MarianMTModel

my_file = open("input.txt", "r", encoding="UTF-8")
text = my_file.read()
my_file.close()

model_name = "Helsinki-NLP/opus-mt-en-uk"

tokenizer = MarianTokenizer.from_pretrained(model_name)

model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

my_file = open("output.txt", "w", encoding="UTF-8")
my_file.write(str(translated_text[0]))
my_file.close()
