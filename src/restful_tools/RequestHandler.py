from django.http import HttpResponse
from django.core import serializers
from urllib import unquote

# handles a request for a collection of item_type
# for ex. example.com/resources/
def HandleStaticCollection(request, item_type, format='json'):
    if request.method == 'GET':
        # return a list of items
        return HttpResponse(serializers.serialize(format, item_type.objects.all()))
    elif request.method == 'PUT':
        # replace the collection with the serialized collection
        for deserialized in serializers.deserialize(format, unquote(request.raw_post_data)):
            deserialized.save()
        return HttpResponse()
    elif request.method == 'POST':
        # create a new entry in the collection
        for deserialized in serializers.deserialize(format, unquote(request.raw_post_data)):
            deserialized.save()
        return HttpResponse()
    elif request.method == 'DELETE':
        # delete the entire collection
        item_type.objecs.all().delete()
        return HttpResponse()
    
# handles a request for a collection of item_type with the item specified
# for ex. example.com/resources/item012
def HandleStaticCollectionWithItem(request, item_type, item, format='json'):
    if request.method == 'GET':
        # return the item specified
        return HttpResponse(serializers.serialize(format, [item_type.objects.get(pk=item)]))
    elif request.method == 'PUT':
        # replace the item specified
        for deserialized in serializers.deserialize(format, unquote(request.raw_post_data)):
            deserialized.save()
        return HttpResponse()   
    elif request.method == 'POST':
        # create a new item
        for deserialized in serializers.deserialize(format, unquote(request.raw_post_data)):
            deserialized.save()
        return HttpResponse()
    elif request.method == 'DELETE':
        # delete the item
        item_type.objects.get(pk=item).delete()
        return HttpResponse()
    
    
# handles a request for a specified collection with the items stored in the attribute field
# for ex. example.com/resource002/
def HandleDynamicCollection(request, collection_type, collection, attribute, format='json'):
    if request.method == 'GET':
        # return the items in the attribute field
        return HttpResponse(serializers.serialize(format, getattr(collection_type.objects.get(pk=collection), attribute).all()))
    elif request.method == 'PUT':
        # replace the entire collection
        for deserialized in serializers.deserialize(format, unquote(request.raw_post_data)):
            deserialized.save()
        return HttpResponse()
    elif request.method == 'POST':
        # create a new item
        for deserialized in serializers.deserialize(format, unquote(request.raw_post_data)):
            deserialized.save()
        return HttpResponse()
    elif request.method == 'DELETE':
        # delete the collection
        collection_type.objects.get(pk=collection).delete()
        return HttpResponse()
    
# handles a request for a specified collection with a specified item
# for ex. example.com/resource002/item012
def HandleDynamicCollectionWithItem(request, collection_type, collection, item_type, item, attribute, format='json'):
    if request.method == 'GET':
        # return the specified item
        return HttpResponse(serializers.serialize(format, [item_type.objects.get(pk=item)]))
    elif request.method == 'PUT':
        # replace the item
        getattr(collection_type.objects.get(pk=collection), attribute).add(item_type.objects.get(pk=item))
        return HttpResponse()
    elif request.method == 'POST':
        # create the item
        getattr(collection_type.objects.get(pk=collection), attribute).add(item_type.objects.get(pk=item))
        return HttpResponse()
    elif request.method == 'DELETE':
        # delete the item
        getattr(collection_type.objects.get(pk=collection), attribute).remove(item_type.objects.get(pk=item))
        return HttpResponse()