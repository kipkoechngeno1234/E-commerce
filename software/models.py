from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
          if not self.slug:
                self.slug = slugify(self.name)
          super().save(*args,**kwargs)
          
    def __str__(self):
              return self.name
    
class Post(models.Model):
      title = models.CharField(max_length=200)
      slug = models.SlugField(unique=True, blank=True)
      content = models.TextField()
      author = models.ForeignKey(User,on_delete=models.CASCADE)
      category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
      created_at = models .DateTimeField(auto_now_add=True)


      def save(self, *args, **kwargs):
            if not self.slug:
                  self.slug = slugify(self.title)
            super().save(*args, **kwargs)

      def __str__(self):
              return self.title
      

class Commment(models.Model):
      post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateField(auto_now_add=True)

      def __str__(self):
             return f"{self.user.username} on {self.post.title}"
