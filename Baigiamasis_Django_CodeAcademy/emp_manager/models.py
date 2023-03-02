from django.db import models



    
class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name



class Employee(models.Model):
    first_name = models.CharField('Vardas', max_length=50)
    last_name = models.CharField('Pavardė', max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField('Telefono Numeris', max_length=20, help_text='Numeris prasideda 86...')
    hire_date = models.DateField('Įsidarbinimo pradžia')
    email = models.EmailField('El. paštas')


    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone}"
   
   

