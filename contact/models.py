from django.db import models
from django.utils import timezone
# id (primary key)
# Create your models here.
# first_name (string), last_name(string),phone (string)
# email (email),createrd_date(date),description(text)


# category (foreign key), owner (foreign key), show (boolean)
# picture(imagem)

# blank=True -> Retira a OBRIGATORIEDADE do campo ser preenchido
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250,blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'