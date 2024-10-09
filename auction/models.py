from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    field= models.CharField(max_length= 64)

    def __str__(self):
        return self.field


class Listings(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owneditems")
    product_name= models.CharField(max_length= 64)
    description= models.CharField(max_length=2048, default='')
    date_time= models.DateTimeField(auto_now=False, auto_now_add=True)
    image= models.CharField(max_length=2048, null=True, blank= True)
    price= models.DecimalField(max_digits= 10, decimal_places=2, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="itemcategory")
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_name}"



class Bid(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bids")
    bid = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_made")

    def __str__(self):
        return f"Latest bid by {self.user}: ₹ {self.bid} [{self.listing}]"
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlists")
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="watchlists")
    added_on = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post= models.ForeignKey(Listings, on_delete=models.CASCADE, related_name= "comments", null= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body= models.TextField()
    post_time= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.author} said: '{self.body}' [{self.post_time}]"
