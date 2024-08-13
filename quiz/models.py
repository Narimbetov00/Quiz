from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    slag = models.SlugField(max_length=150,unique=True)

    class Meta:
        ordering = ('id',)
        verbose_name= 'Category'
        verbose_name_plural='Categories'
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('category',kwargs={'category_slug':self.slag})

class Test(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True,max_length=150)
    discription = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name= 'Test'
        verbose_name_plural='Tests'
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('category',kwargs={'test_slug':self.slug,'category_slug':self.category.slag})   

class Questions(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        ordering = ('id',)
        verbose_name= 'Question'
        verbose_name_plural='Questions'
    def __str__(self) -> str:
        return f'{self.test}-{self.id}'
    

class Answer(models.Model):
    answer = models.CharField(max_length=150)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    class Meta:
        ordering = ('id',)
        verbose_name= 'Answer'
        verbose_name_plural='Answers'
    def __str__(self) -> str:
        return self.answer
             

    
    



