from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView, CreateView

from .forms import AddNews, UserForm, CommentForm
from .models import *
from .utils import MyMixin



# Главная страница
class HomePage(MyMixin, ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mixin_reg'] = self.get_reg()
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

def back(request):
    return redirect('/')


def feedback(request):
    context = {
        'title': 'Обратная свзяь'
    }
    return render(request, 'feedback.html', context=context)

# Добавление новости
class AddPost(CreateView):
    form_class = AddNews
    template_name = 'add_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить новость'
        return context

# Авторизация
class LoginUser(LoginView):
    form_class = AuthenticationForm             # Стандартная django Форма
    template_name = 'login.html'

    def get_success_url(self):                  # При авторизации перенаправит на '/home'
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Авторизация'
        return context

def logout_user(request):
    logout(request)
    return redirect('login')

# Регистрация пользователей
class RegisterUser(CreateView):
    form_class = UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    # автомотическая авторизация при регистрации
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('home')

# Просмотр новостей
class ShowNews(DeleteView):
    model = News
    template_name = 'show_news.html'
    context_object_name = 'news'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(slug=self.kwargs['news_slug'])
        return context


# Просмотр категорий
class ShowCategory(ListView):
    model = News
    template_name = 'home.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['cat_slug'])
        return context

    # Выводит категории по слагу без этой ф-ии будут выводиться все категории
    def get_queryset(self):
        return News.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)


# Добавление комментария
class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        news = News.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = news
            form.save()
        return redirect(news.get_absolute_url())

