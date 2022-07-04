from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='John Doe')
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Books"
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Grocery(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, related_name='grocery', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    imageurl = models.URLField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Groceries"
        ordering = ['-date_created']

    def __str__(self):
        return self.name
