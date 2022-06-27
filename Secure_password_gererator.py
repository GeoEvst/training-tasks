from random import randint, sample
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_characters = '!#$%&*+-=?@^_'


# проверка правильности введенных значений
def config_is_valid(config):
    val_1 = True
    val_2 = True
    cnt_1 = 0
    cnt_2 = 0
    for i in range(len(config)):
        if i < 2 and config[i].isdigit():
            cnt_1 += 1
        if i >= 2 and (config[i].lower() == 'да' or config[i].lower() == 'нет'):
            cnt_2 += 1
    if cnt_1 != 2:
        val_1 = False
    if cnt_2 != 5:
        val_2 = False
    return val_1 == val_2 is True


# ввод пользователем конфигурации для генерации пароля
def set_conditions():
    config = list()
    cnt = 0
    print('Введите условия через нажатие "Enter":', '\n'
          '1) Сколько паролей вам сгенерировать? Введите число;', '\n'
          '2) Сколько символов должно быть? Введите число;', '\n'
          '3) Использовать цифры? Введите "Да" или "Нет;"', '\n'
          '4) Использовать строчные буквы? Введите "Да" или "Нет;"', '\n'
          '5) Использовать прописные буквы? Введите "Да" или "Нет;"', '\n'
          '6) Использовать спецсимволы? Введите "Да" или "Нет;"', '\n'
          '7) Исключить неоднозначные символы? Введите "Да" или "Нет;"', '\n')
    while len(config) != 7:
        cnt += 1
        print(cnt, ')', sep='')
        config.extend(input().split())
    if config_is_valid(config) is False:
        print('Введены недопустимые значения, повторите попытку.')
        return False
    else:
        return config


# составление набора возможных значений на основании конфигурации
def possible_values(config):
    chars = ''
    if config[2].lower() == 'да':
        chars = chars + digits
    if config[3].lower() == 'да':
        chars = chars + lowercase_letters
    if config[4].lower() == 'да':
        chars = chars + uppercase_letters
    if config[5].lower() == 'да':
        chars = chars + special_characters
    if config[6].lower() == 'да':
        chars = chars.replace('0', '')
        chars = chars.replace('i', '')
        chars = chars.replace('l', '')
        chars = chars.replace('1', '')
        chars = chars.replace('L', '')
        chars = chars.replace('o', '')
    return config[0], config[1], chars


# генерация паролей
def generate_password(n, length, chars):
    passwords = list()
    password_str = ''
    for i in range(int(n)):
        password = sample(chars, int(length))
        password_str = password_str.join(password)
        passwords.append(password_str)
        password_str = ''
    return passwords


config = set_conditions()
n, lenght, chars = possible_values(config)
password = generate_password(n, lenght, chars)
print(*password, sep='\n')