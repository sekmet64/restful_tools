from django.db.models import Model, CharField, ManyToManyField, DateField, BigIntegerField, TextField

class Book(Model):
    ISBN = BigIntegerField(primary_key=True)
    title = CharField(max_length = 100)
    published = DateField()
    description = TextField()
    
    def __unicode__(self):
        return self.title
    
class Bookshelf(Model):
    name = CharField(max_length = 100, primary_key=True)
    books = ManyToManyField(Book, blank=True)
    
    def __unicode__(self):
        return self.name