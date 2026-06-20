from django.db import models

# Education model - stores degree information
class Education(models.Model):
    degree = models.CharField(max_length=100)        # e.g. "BS Computer Science"
    institute = models.CharField(max_length=200)     # e.g. "FAST University"
    session = models.CharField(max_length=50)        # e.g. "2020 - 2024"
    description = models.TextField()                  # Extra details

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name_plural = "Education"