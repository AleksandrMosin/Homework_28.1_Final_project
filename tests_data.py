from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    first_name_1_char = 'И'
    first_name_31_char = 'Иваниваниваниваниваниваниванива'
    last_name_1_char = 'И'
    last_name_31_char = 'Иваниваниваниваниваниваниванива'
    password_21_char = 'Qwerty0Qwerty0Qwerty0'
    password_no_Lower = 'qwerty10'
    password_9_char = 'Qwertyu10'
    password_not_contain_digit = "Qwertyui"
    xss = '<script>alert(123)</script>'
    email_without_domain = 'test@.ru'
    invalid_phoneNumber = '+79999999999'

class Valid_Data:
    valid_first_name = 'Иван'
    valid_last_name = 'Иванов'
    valid_password = 'Qwerty10!'
    valid_phoneNumber = '+79263964647'
    valid_email = 'sword444@mail.ru'