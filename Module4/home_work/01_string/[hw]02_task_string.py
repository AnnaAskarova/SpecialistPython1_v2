# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"

text = input("Введите текст: ")
text = text.lower() + " "
amount_index = len(text) - 1

first_b = text.find("б")
if first_b == -1:
    print("слов на б нет")
else:
    i = first_b
    while text[i] != " ":
        print(text[i], end="")
        if i == amount_index:
            i = 0
        i += 1
