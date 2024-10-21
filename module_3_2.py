def send_email(message, recipient, *, sender='university.help@gmail.com'):
    check = ('.com', '.ru', '.net')
    check_dog = '@'

    # if not (sender.index(check_dog) and recipient.index(check_dog) and sender.endswith(check) and recipient.endswith(check)):
    if not (check_dog in sender and check_dog in recipient and sender.endswith(check) and recipient.endswith(check)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender.count(check_dog) > 1 or recipient.count(check_dog) > 1:
        print(f'Адрес {sender} или {recipient} содержит больше одного символа @')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif not sender == 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')