from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        # Esta funcion devuelve la url products_by_category es el nombre de la url (dentro de store) + el slug. Genera por ejemplo : http://localhost:8000/store/computer 
        return reverse('products_by_category', args=[self.slug])
        

    def __str__(self):
        return self.category_name

