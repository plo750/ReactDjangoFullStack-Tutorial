from django.db import models


# Create your models here.
class Book(models.Model):
    """

    null=True =/= blank=False
    default='' ==> No sense with null=True first because the default will never be triggered
    choices BOOKS = [
        ('HB', 'Hobbit'),
        ('',''),
        ('','')
        ] ==> Acceptable values tupple
        usage ==> choices=BOOKS
    """
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)

    # price2 = models.DecimalField(default=0,decimal_places=2) same with models.FloatField
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)

    # auto_now=True ==> On save the date will be updated
    # auto_now_add ==> Only when created the date will be updated
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)

    #def __str__(self):
    #    return self.title

