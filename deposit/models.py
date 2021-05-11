from django.db import models
# from deposit_project.depozits import Deposit1


class Deposit(models.Model):

    deposit = models.CharField(max_length=20)
    term = models.CharField(max_length=10)
    rate = models.CharField(max_length=10)
    interest = models.CharField(max_length=10)



