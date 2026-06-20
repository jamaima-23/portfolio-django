from django.db import models

# Projects model - stores portfolio projects
class Project(models.Model):
    title = models.CharField(max_length=200)          # e.g. "E-commerce Website"
    technologies = models.CharField(max_length=200)   # e.g. "Django, Bootstrap"
    description = models.TextField()                   # Project details
    link = models.URLField(blank=True, null=True)     # Optional project URL

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"