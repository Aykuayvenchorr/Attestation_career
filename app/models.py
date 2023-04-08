from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.exceptions import ValidationError


from app.validators import password_validator, validate_allowed_domains, validate_post_title


def validate_author_age(instance):
    """
    Валидатор для проверки возраста автора поста (должен быть старше 18 лет).
    """
    age = timezone.now().date().year - User.objects.get(id=instance).birth_date.year
    if age < 18:
        raise ValidationError('Автор поста должен быть старше 18 лет.')


class BaseModel(models.Model):
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.TextField(validators=[password_validator])
    email = models.EmailField(validators=[validate_allowed_domains])
    phone_number = PhoneNumberField(blank=True)
    birth_date = models.DateField(null=True)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username}"


class Comment(BaseModel):
    author = models.ForeignKey(User, on_delete=CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text


class Post(BaseModel):
    title = models.CharField(max_length=50, validators=[validate_post_title])
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=CASCADE, validators=[validate_author_age])
    comments = models.ManyToManyField(Comment, null=True, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title









