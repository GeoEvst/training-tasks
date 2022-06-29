import time

# Сдвиг алфавита
def alphabet_shift(k, n):
    shift = list()
    if k > 0:
        for i in range(n - k):
            shift.extend(chars[i + k])
        shift.extend(chars[:k])
    if k <= 0:
        for j in range(n):
            shift.extend(chars[j + k])
    return shift


# Шифрование открытого текста
def text_encryption(plaintext, alphabet_shift):
    index_plaintext = list()
    text_characters = list()
    index_upper_case = list()
    chip = list()

    for i in range(len(plaintext)):
        if plaintext[i].isupper():
            index_upper_case.append(i)
        if not plaintext[i].isalpha() and not plaintext[i].isdigit():
            text_characters.append(i)
        if plaintext[i].isalpha():
            index_plaintext.append(chars.index(plaintext[i].upper()))

    for i in index_plaintext:
        chip.extend(alphabet_shift[i].lower())

    for i in text_characters:
        chip.insert(i, plaintext[i])

    for i in index_upper_case:
        chip.insert(i, chip[i].upper())
        del chip[i + 1]
    return chip


def hack(n):
    for i in range(1, n):
        alphabet_shift_1 = alphabet_shift(i, n)
        ciphertext = text_encryption(plaintext, alphabet_shift_1)
        print(*ciphertext, sep='')



'''
# выбор алфавита Eng или Rus
def set_localization(shift_laue, n):
    if shift_value.isdigit():
        k = int(shift_value)
        if loc == 0:
            alphabet_shift = alphabet_shift_rus(k)
            ciphertext = text_encryption(plaintext, alphabet_shift)
            print(*ciphertext, sep='')
        elif loc == 1:
            alphabet_shift = alphabet_shift_eng(k, n)
            ciphertext = text_encryption(plaintext, alphabet_shift)
            print(*ciphertext, sep='')
    elif shift_value.lower() == 'no':
        for i in range(1, 26):
            alphabet_shift = alphabet_shift_eng(i, n)
            ciphertext = text_encryption(plaintext, alphabet_shift)
            print(*ciphertext, sep='')'''


print('Введите "0" если тест на русском языке, "1" если на английском')
loc = int(input())
chars = list()
n = 0
k = 0

print('Введите текст')
plaintext = input()

if loc == 0:
    chars = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
                  'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    print('Введите сдвиг от 1 до 32, если не знаете введите "0", чтобы перебрать все варианты.')
    shift_value = input()
    if shift_value == '0':
        hack(32)
    else:
        k = int(shift_value)
        alphabet_shift = alphabet_shift(k, 32)
        ciphertext = text_encryption(plaintext, alphabet_shift)
        print(*ciphertext, sep='')

elif loc == 1:
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    print('Введите сдвиг от 1 до 26, если не знаете введите "0", чтобы перебрать все варианты.')
    shift_value = input()
    if shift_value == '0':
        hack(26)
    else:
        k = int(shift_value)
        alphabet_shift = alphabet_shift(k, 26)
        ciphertext = text_encryption(plaintext, alphabet_shift)
        print(*ciphertext, sep='')
else:
    print('Ошибка, начните заново и ВНИМАТЕЛЬНО прочитайте подсказки в консоли')

time.sleep(60)
