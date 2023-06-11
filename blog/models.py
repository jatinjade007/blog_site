from django.db import models

# Create your models here.

# Blog Table
class Blogs(models.Model):
    blog_id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=150)

    def __str__(self):
        return self.blog_title


# Blog Content table
class Blog_Content(models.Model):
    blog_content_id = models.IntegerField(primary_key=True)
    blog_content = models.TextField()
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_content_id


# Blog Content's Comments Table
class Comments(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    comment = models.TextField()
    blog_content = models.ForeignKey(Blog_Content, on_delete=models.CASCADE)

    def __str__(self):
        return self.Comment
    