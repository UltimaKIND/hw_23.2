from django.contrib import admin
from users.models import User

# Регистрация модели User в панели администратора 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'country', 'token', 'password')
    actions = ["delete_selected"]
