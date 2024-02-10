from django.db import models


class Lavozim(models.Model):
    nom = models.CharField(max_length=250)
    maosh = models.PositiveIntegerField()
    def __str__(self):
        return self.nom


class Xona(models.Model):
    raqam = models.PositiveIntegerField()
    necha_orinli = models.PositiveIntegerField()
    bosh = models.BooleanField()
    hona_turi = models.CharField(max_length=250,choices=[("Standart","Standart"),("Luxe","Luxe")])
    narx = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.raqam}, {self.bosh}"


class Xodim(models.Model):
    ism = models.CharField(max_length=250)
    yosh = models.PositiveIntegerField()
    lavozim = models.ForeignKey(Lavozim, on_delete=models.CASCADE)
    ish_vaqti = models.CharField(max_length=250)
    xona = models.ForeignKey(Xona,on_delete=models.CASCADE, blank=True,null=True)
    tel_raqam = models.CharField(max_length=17)
    manzil = models.TextField()

    def __str__(self):
        return f"{self.ism}: {self.lavozim}"


class Buyurtma(models.Model):
    xodim = models.ForeignKey(Xodim,on_delete=models.CASCADE)
    mijoz = models.CharField(max_length=250)
    xona = models.ForeignKey(Xona, on_delete=models.CASCADE)
    olingan_sana = models.DateField()

    def __str__(self):
        return f"Bron qilingan nona raqami:{self.xona}"


