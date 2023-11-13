from django.db import models

class FileCheck(models.Model):
    file = models.FileField(upload_to="text")