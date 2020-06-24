'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

'''

my_file = open("First1.txt", "r", encoding="utf-8")

content = my_file.readlines() # реадлайнс переводит в список
for i, item in enumerate(content, 1): # перебор через цикл fgor _ in _ используя enumirate( предоставляет данные по индексу и по значению)
    new = item.split()
    print(f"Строка№{i} - В ней - {len(new)} слова(ов)")
print(content)

my_file.close()


