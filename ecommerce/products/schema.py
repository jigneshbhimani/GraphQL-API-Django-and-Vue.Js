# A schema is a contract between the client and the server that describes how the client can acquire access to the database.
# created a schema for our three models (Category, Book, and Grocery).
# included DjangoObjectType: which uses GraphQL to display all fields on a Model.
# class Query: inherits from ‘graphene.ObjectType’ and provides the setting for our Graphql queries.
# resolve_categories, resolve_books, resolve_groceries: are used to open up categories, books, groceries queryset. These methods take in two parameters (root and info).
# graphene.Schema: this query brings in data from our type(database).

from unicodedata import decimal
import graphene
from graphene_django import DjangoObjectType
from products.models import Category, Book, Grocery


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'pages',
            'price',
            'quantity',
            'description',
            'status',
            'date_created'
        )


class GroceryType(DjangoObjectType):
    class Meta:
        model = Grocery
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'quantity',
            'imageurl',
            'status',
            'date_created'
        )


# For Fetching
class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)
    groceries = graphene.List(GroceryType)

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_books(root, info, **kwargs):
        return Book.objects.all()

    def resolve_groceries(root, info, **kwargs):
        return Grocery.objects.all()


# ‘class argument’ allows us to define a parameter to save data to the database.
# ‘class Mutation’ defines our mutations and sends parameters such as updating and creating data to the model.


# Update Category
class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category
        title = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()

        return UpdateCategory(category=category)


# Create Category
class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()

        return CreateCategory(category=category)


# Delete Category
class DeletCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, id):
        category_instance = Category.objects.get(pk=id)
        category_instance.delete()

        return None


# Book Input
class BookInput(graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    pages = graphene.Int()
    price = graphene.Int()
    quantity = graphene.Int()
    description = graphene.String()
    status = graphene.String()


# Create Book
class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title
        book.author = input.author
        book.pages = input.pages
        book.price = input.price
        book.quantity = input.quantity
        book.description = input.description
        book.status = input.status
        book.save()

        return CreateBook(book=book)


# Update Book
class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, title, id):
        book = Book.objects.get(pk=id)
        book.name = input.name
        book.description = input.description
        book.price = decimal.Decimal(input.price)
        book.quantity = input.quantity
        book.save()

        return UpdateBook(book=book)


# Delete Book
class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        book_instance.delete()

        return None


# we updated our schema by adding mutation to the Schema constructor.
# For Update and Create
class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    delete_category = DeletCategory.Field()
    update_book = UpdateBook.Field()
    create_book = CreateBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
