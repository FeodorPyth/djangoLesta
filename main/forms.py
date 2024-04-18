from django import forms


class FileFieldForm(forms.Form):
    """Класс формы для загрузки текстового файла."""
    file_field = forms.FileField()
  
