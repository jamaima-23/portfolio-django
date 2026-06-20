from django.db import models

# Experience model - stores work experience
class Experience(models.Model):
    organization = models.CharField(max_length=200)  # e.g. "Google"
    position = models.CharField(max_length=100)      # e.g. "Junior Developer"
    duration = models.CharField(max_length=100)      # e.g. "Jan 2023 - Dec 2023"
    description = models.TextField()                  # Job responsibilities

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name_plural = "Experience"