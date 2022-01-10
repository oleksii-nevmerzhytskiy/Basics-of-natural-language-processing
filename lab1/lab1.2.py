import re


def non_letter(str):
    return re.sub("[0-9\W_]", " ", str)


def get_unique(text):
    unique = []
    for word in text:
        if word not in unique:
            unique.append(word)
    return unique


def to_id(str, dict):
    id = []
    for word in str:
        id.append(dict[word])
    return id


my_file = open("input1.txt", "r", encoding="UTF-8")
my_string = my_file.read()
my_file.close()
print(my_string)

my_string = non_letter(my_string)
my_string = my_string.lower()
my_string = my_string.split()

unique = get_unique(my_string)

dictionary = {unique[i]: i for i in range(len(unique))}

id = to_id(my_string, dictionary)

print(id)
my_file = open("output1.txt", "w", encoding="UTF-8")
for i in id:
    my_file.write(str(i) + " ")
my_file.close()
