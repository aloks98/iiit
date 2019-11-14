from django.db import models
from datetime import datetime

from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Society(models.Model):
    soc_id = models.CharField(max_length=5, primary_key=True)
    soc_name = models.CharField(max_length=20)
    net_amount_issued = models.IntegerField()
    amount_left = models.IntegerField()
    dues = models.IntegerField()

    def __str__(self):
        return self.soc_name

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.soc_id)])


class Secretaries(models.Model):
    sec_id = models.CharField(max_length=6, primary_key=True)
    soc_id = models.ForeignKey(Society, on_delete=models.CASCADE)
    type_of_account = models.CharField(max_length=1, null=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=64)
    year = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.name, self.soc_id)


class Proposals(models.Model):
    proposal_no = models.IntegerField(primary_key=True)
    soc_id = models.ForeignKey(Society, on_delete=models.CASCADE)
    # sec_id = models.ForeignKey(Secretaries, on_delete=models.CASCADE)
    net_amount_left = models.IntegerField()
    amount_asked_for = models.IntegerField()
    amount_returned = models.IntegerField()
    purpose = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Proposal no. {} - {}".format(self.proposal_no, self.soc_id)
