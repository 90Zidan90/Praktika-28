valid_email = "zidan.90@yandex.ru"
valid_pass = "Zidan19901802"

invalid_email = 'zidanius.90@yandex'
invalid_pass = 'ЗИдан18021990'

name = 'Александр'
surname = 'Куприянов'
region = 'Кострома г'
email = 'zidan.90@yandex.ru'
password = 'Zidan19901802'

false_email = 'Z1990'
false_mobile_max = '896100885920'
false_mobile_mini = '8961008859'
false_name_mini = 'И'
name_two_letters = "Га"
thirty_letters = 'рволаьктсрмзцлатчбашкгвочьсоюб'
thirty_one_letters = 'ладызкщушчлвьмостчрвдыжчбычшящз'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'