import json

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.base import View

from core.services import api_mybook


class AppView(TemplateView):
    template_name = "core/books.html"


class AuthView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        session = api_mybook.auth(data['email'], data['password'])

        response = HttpResponse()
        response.set_cookie('session', session, domain=settings.SESSION_COOKIE_DOMAIN)

        return response


class BooksView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        session = request.COOKIES.get('session')
        page = request.GET.get('page')
        books, meta = api_mybook.get_books(session, page)

        return JsonResponse({
            'books': books,
            'meta': meta,
        })
