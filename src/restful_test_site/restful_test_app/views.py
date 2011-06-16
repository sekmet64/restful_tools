from django.shortcuts import render_to_response
from models import Bookshelf, Book
from django.views.decorators.csrf import csrf_exempt
from restful_tools.RequestHandler import HandleStaticCollection, HandleDynamicCollection, HandleDynamicCollectionWithItem, HandleStaticCollectionWithItem

def index(request):
    return render_to_response('restful_test/index.html')

@csrf_exempt
def api(request, bookshelf, book):
    
    if book != '':
        return HandleDynamicCollectionWithItem(request, Bookshelf, bookshelf, Book, book, 'books')

    if bookshelf != '':
        return HandleDynamicCollection(request, Bookshelf, bookshelf, 'books')
    
    return HandleStaticCollection(request, Bookshelf)
    
@csrf_exempt    
def books(request, book):
    if book != '':
        return HandleStaticCollectionWithItem(request, Book, book)
    
    return HandleStaticCollection(request, Book)