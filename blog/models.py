from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    author = models.CharField("Author",max_length=20)
    title = models.CharField("Title",max_length=30)
    content = RichTextField()
    image = models.FileField(blank=True,null=True,verbose_name="image:")



    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name= "comments")
    comment_author = models.CharField("Name",max_length=50)
    comment_content = models.CharField("Comment",max_length=250)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_author
    class Meta:
        ordering = ["-comment_date"]