from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200, unique=True)   # పాట పేరు
    lyrics = models.TextField()                             # సాహిత్యం

    def __str__(self):
        return self.title
