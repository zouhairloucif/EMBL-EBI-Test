from django.db import models


# Create your models here.

class Molecule(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200)
    max_phase = models.IntegerField(default=0)
    structure = models.CharField(max_length=200)
    inchi_key = models.CharField(max_length=27)

    def __str__(self):
        return self.name


class Target(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200)
    organism = models.CharField(max_length=200)

    def __str__(self):
        return "Type: %s" % self.name


class Activity(models.Model):
    objects = models.Manager()
    type = models.CharField(max_length=250)
    units = models.CharField(max_length=100)
    value = models.FloatField(default=0)
    relation = models.CharField(max_length=2)
    target_id = models.ForeignKey(Target, on_delete=models.CASCADE, related_name='targets')
    molecule_id = models.ForeignKey(Molecule, on_delete=models.CASCADE, related_name='activities')

    def __str__(self):
        return "Type: %s, Value: %s" % (self.type, self.value)