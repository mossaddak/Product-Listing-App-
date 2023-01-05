from django.db import models
from userProfileApp.models import User

# product image function
def upload_product_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="productsRelatedName", blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(blank=True, null=True, max_length=50)
    image = models.ImageField(upload_to=upload_product_image, null=True, blank=True)
    def __str__(self):
        return f"{self.pk}.{self.user.username}({self.title})"








