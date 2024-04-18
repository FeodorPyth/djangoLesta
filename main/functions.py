import os
import math

from django.conf import settings

from main.models import Word


def load_file(file_name):
    """Функция для загрузки файла в медиа."""
    with open(os.path.join(settings.MEDIA_ROOT, file_name.name), 'wb') as f:
        for chunk in file_name.chunks():
            f.write(chunk)


def count_words(file_path):
    """Функция для подсчета повторений слов."""
    words = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.strip().split():
                if word not in words:
                    words[word] = 0
                words[word] += 1
    return words


def create_words(word_data):
    """Функция для расчета idf и создания записей в БД."""
    for word, tf in word_data.items():
        idf = round(math.log(1 + (len(Word.objects.all()) / (1 + tf))), 2)
        Word.objects.create(word=word, tf=tf, idf=idf)
