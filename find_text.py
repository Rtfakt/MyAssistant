import re

def scan_text (text):
    scan = []
    # Использование регулярных выражений для поиска:
    scan.append(re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}', text)[1])
    scan.extend(re.findall(r'[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+', text)[0].split()[0:3])
    scan.append(re.findall(r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}', text)[2])
    return scan


# Считываем текст из файл
with open("example_texts/1.txt", encoding="UTF-8") as f:
    text = f.read()

s = scan_text(text)

print(s) #Выводит список из 5 элементов, можно обратиться к каждому элементу:
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])