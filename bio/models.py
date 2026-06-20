from django.db import models

# Bio model - stores personal information
class Bio(models.Model):
    name = models.CharField(max_length=100)           # Full name
    job_title = models.CharField(max_length=100)      # e.g. "Web Developer"
    profile_picture = models.ImageField(upload_to='profile/')  # Profile image
    description = models.TextField()                   # Professional description

    def __str__(self):
        return self.name  # Shows name in admin panel

    class Meta:
        verbose_name_plural = "Bio"  # Label in admin