# cookbook/ingredients/schema.py
import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from book_info.models import Book_info, Catagory

# Graphene will automatically map the Catagory model's fields onto the CatagoryNode.
# This is configured in the CatagoryNode's Meta class (as you can see below)

class CatagoryNode(DjangoObjectType):
    class Meta:
        model = Catagory
        filter_fields = ['name', 'book_infos']
        interfaces = (relay.Node, )


class Book_infoNode(DjangoObjectType):
    class Meta:
        model = Book_info
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'catagory': ['exact'],
            'catagory__name': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    catagory = relay.Node.Field(CatagoryNode)
    all_catagories = DjangoFilterConnectionField(CatagoryNode)

    book_info = relay.Node.Field(Book_infoNode)
    all_book_infos = DjangoFilterConnectionField(Book_infoNode)
