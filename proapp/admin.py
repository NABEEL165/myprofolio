
from django.contrib import admin

# Register your models here.


from .models import ContactMessage   # 👈 Import your model

admin.site.register(ContactMessage)  