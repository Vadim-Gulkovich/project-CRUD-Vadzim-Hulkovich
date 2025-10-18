import json
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from books.models import Book


def parse_body(request):
    try:
        return json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return request.POST


@method_decorator(csrf_exempt, name='dispatch')
class BookList(View):
    
    def get(self, request):
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class BookDetail(View):
    
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        return JsonResponse(model_to_dict(book), status=200)


@method_decorator(csrf_exempt, name='dispatch')
class BookAdd(View):
    
    def post(self, request):
        data = parse_body(request)
        title = data.get("title")
        author = data.get("author")
        published_date = data.get("published_date")
        pages = data.get("pages")
        price = data.get("price")
        category = data.get("category")

        if not title or not author or not published_date or not pages or not category or not price:
            return JsonResponse({"error": "Title, author, published_date, price, category and pages are required."}, status=400)

        book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            pages=pages,
            price=price, 
            category=category
        )
        return JsonResponse(model_to_dict(book), status=201)


@method_decorator(csrf_exempt, name='dispatch')
class BookUpdate(View):
    
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        data = parse_body(request)

        book.title = data.get("title", book.title)
        book.author = data.get("author", book.author)
        book.published_date = data.get("published_date", book.published_date)
        book.pages = data.get("pages", book.pages)
        book.price = data.get("price", book.price)
        book.category = data.get("pagcategoryes", book.category)
        book.save()

        return JsonResponse(model_to_dict(book), status=200)


@method_decorator(csrf_exempt, name='dispatch')
class BookDelete(View):
    
    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()
        return JsonResponse({"message": "Book deleted successfully."}, status=200)
