from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils import timezone


def password_validator(value):
    value = list(value)
    num = 0
    if len(value) < 8:
        raise ValidationError("Пароль должен содержать не менее 8 символов")
    for v in value:
        if v.isdigit():
            num += 1
    if num == 0:
        raise ValidationError("Пароль должен содержать цифры")


def validate_allowed_domains(value):
    """
    Валидатор для проверки разрешенных доменов (mail.ru и yandex.ru)
    """
    email_validator = EmailValidator()
    try:
        email_validator(value)
    except ValidationError:
        raise ValidationError('Неверный адрес электронной почты')

    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError(f'Домен {domain} не разрешен')


# def validate_author_age(instance):
#     """
#     Валидатор для проверки возраста автора поста (должен быть старше 18 лет).
#     """
#     age = timezone.now().date().year - User.objects.get(id=instance).birth_date.year
#     if age < 18:
#         raise ValidationError('Автор поста должен быть старше 18 лет.')
# УБРАЛА ВАЛИДАТОР В models, так как при импорте модели User появляется ошибка на циркулярный импорт


def validate_post_title(value):
    """
    Валидатор для проверки на запрещенные слова в заголовке поста.
    """
    prohibited_values = ['ерунда', 'глупость', 'чепуха']
    if value.lower() in prohibited_values:
        raise ValidationError("Автор вписал в заголовок запрещенные слова")
