
def custom_write(file_name, strings):
    strings_positions = dict()

    with open(file_name, "w", encoding="utf-8") as f:
        for i in range(len(strings)):
            strings_positions[(i + 1, f.tell())] = strings[i]
            f.write(f'{strings[i]}\n')

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

print(result)