from .models import *

menu = [
    {'title': 'Главная страница', 'url_name': 'main:home'},
    {'title': 'Добавить трек', 'url_name': 'main:add'}
]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['cats'] = Categories.objects.all()
        return context
