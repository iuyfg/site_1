import os
import django

# Настраиваем окружение Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korochki.settings')
django.setup()

from django.contrib.auth.models import User

# Данные для админа
USERNAME = 'admin'
EMAIL = 'admin@example.com'
PASSWORD = 'admin123456' # Придумайте надежный пароль!

try:
    user = User.objects.get(username=USERNAME)
    print(f"Пользователь '{USERNAME}' уже существует.")
except User.DoesNotExist:
    user = User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print(f"✅ Суперпользователь '{USERNAME}' успешно создан!")
    print(f"Логин: {USERNAME}")
    print(f"Пароль: {PASSWORD}")