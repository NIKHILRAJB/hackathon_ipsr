from django.db import models


class Employee(models.Model):
    # ecode = models.ForeignKey(ename, on_delete=models.CASCADE)
    ename = models.CharField(max_length=100)
    edep = models.CharField(max_length=200)
    ecode = models.IntegerField(max_length=10)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.ename
# Create your models here.
