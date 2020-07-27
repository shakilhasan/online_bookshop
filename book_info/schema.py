# cookbook/ingredients/schema.py
import graphene

from graphene_django.types import DjangoObjectType
from book_info.models import Book_info, Catagory

class CatagoryType(DjangoObjectType):
    class Meta:
        model = Catagory


class Book_infoType(DjangoObjectType):
    class Meta:
        model = Book_info


class Query(object):
    catagory = graphene.Field(CatagoryType, id=graphene.Int(), name=graphene.String())
    book_info = graphene.Field(Book_infoType, id=graphene.Int(), name=graphene.String())
    all_catagories = graphene.List(CatagoryType)
    all_Book_infos = graphene.List(Book_infoType)

    def resolve_all_catagories(self, info, **kwargs):
        return Catagory.objects.all()

    def resolve_all_book_infos(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Book_info.objects.select_related('catagory').all()

    def resolve_catagory(self, info, **kwargs):
      id = kwargs.get('id')
      name = kwargs.get('name')

      if id is not None:
          return Catagory.objects.get(pk=id)

      if name is not None:
          return Catagory.objects.get(name=name)

      return None

    def resolve_book_info(self, info, **kwargs):
      id = kwargs.get('id')
      name = kwargs.get('name')

      if id is not None:
          return Book_info.objects.get(pk=id)

      if name is not None:
          return Book_info.objects.get(name=name)

      return None
