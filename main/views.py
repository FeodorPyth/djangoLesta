import os

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import FileFieldForm
from .functions import count_words, create_words, load_file
from .models import Word


class UploadFileView(View):
    """Вью-класс для обработки загруженных файлов."""
    def get(self, request):
        form = FileFieldForm()
        return render(request, template_name='main/upload.html', context={'form': form})

    def post(self, request):
        form = FileFieldForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file_field']
            if file.name not in os.listdir(settings.MEDIA_ROOT):
                load_file(file_name=file)
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            words = count_words(file_path=file_path)
            Word.objects.all().delete()
            create_words(word_data=words)
            return redirect('main:result')
        return render(request, template_name='main/upload.html', context={'form': form})


class ResultView(TemplateView):
    """Вью-класс для вывода итоговой таблицы."""
    template_name = 'main/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_number = self.request.GET.get('page')
        words = Word.objects.all()[:50]
        paginator = Paginator(words, 10)
        page_obj = paginator.get_page(page_number)
        context['words'] = page_obj
        return context


class RulesTemplateView(TemplateView):
    """Вью-класс для страницы правил."""
    template_name = 'main/rules.html'
