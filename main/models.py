from django.db import models








class CategoriyaBook(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title




class Book(models.Model):
    categoriyabook  = models.ForeignKey(CategoriyaBook, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    book_download = models.FileField(upload_to ='book/')


    def __str__(self):
        return self.title

