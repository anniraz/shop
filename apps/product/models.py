from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe


# Create your models here.

class Category(MPTTModel):
    STATUS_CHOICES=(
        ('True','True'),
        ('False','False'))

    title=models.CharField(max_length=50,unique=True)
    parent=TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    image=models.ImageField(upload_to="category")
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default=True)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return f'{self.title}'

    class MPTTMeta:
        order_insertion_by = ['title']


    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

            
    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})

class Product(models.Model):
    STATUS_CHOICES=(
        ('True','True'),
        ('False','False'))

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True ,verbose_name='Категория')
    title=models.CharField(max_length=100)
    price=models.IntegerField(blank=True,null=True)
    description=RichTextUploadingField()
    image=models.ImageField(upload_to="products/")
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default=True)
    slug=models.SlugField(unique=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height=50px >'.format(self.image.url))
        else:
            return ""


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50px">'.format(self.image.url))
        else:
            return "" 
    

class Review(models.Model):
    RATING_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        max_length=255
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    text = models.TextField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='review_product',
    )
    rating = models.CharField(
        max_length=5,
        choices=RATING_CHOICE,
    )



    def __str__(self):
        return f'{self.name}: {self.rating}'




