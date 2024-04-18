from django.urls import path
from .views import ResultView, RulesTemplateView, UploadFileView


app_name = 'main'

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('rules/', RulesTemplateView.as_view(), name='rules'),
    path('result/', ResultView.as_view(), name='result')
]
