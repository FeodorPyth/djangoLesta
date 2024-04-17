from django.conf import settings
from django.db import models


class Word(models.Model):
    """Модель для слов из загружаемых документов."""
    word = models.CharField(
        max_length=settings.MAX_LENGTH_WORD,
        verbose_name='Слово'
    )
    tf = models.PositiveIntegerField()
    idf = models.FloatField()

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
        ordering = ['-idf']

    def __str__(self):
        return self.word
