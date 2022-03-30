from django.db import models

class Resto(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=80)
    type = models.CharField(max_length=20)


    def __str__(self):
        return "{}".format(self.name)

class Usaha(models.Model):

    pilih =(
    ("Halal", "Halal"),
    ("Non-Halal", "Non-Halal"),
)
    Resto = models.OneToOneField(
        Resto,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    employee_n = models.IntegerField(default=False)
    area = models.FloatField(default=False)
    year_e = models.IntegerField(default=False)
    halal = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.Resto.name)
