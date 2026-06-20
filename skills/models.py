from django.db import models

# Skills model - stores skill and its level
class Skill(models.Model):
    name = models.CharField(max_length=100)          # e.g. "Python"
    percentage = models.IntegerField()               # e.g. 85 (means 85%)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skills"