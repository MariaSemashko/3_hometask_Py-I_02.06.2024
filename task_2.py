'''В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания и
регистр символов.За основу возьмите любую статью из википедии или
из документации к языку.'''

import re

TOP = 10

text = (input('Введите строку: ')).lower()
text = re.sub(r'[^\w\s]','', text)
text = text.split()

result = {item: text.count(item) for item in text}
result = sorted(result.items(), key=lambda item: item[1], reverse=True)

print()
print(f'Количество встречаемых слов: {len(result)}, \n'
      f'10 самых частых слов в порядке убывания: {result[0:TOP]}')