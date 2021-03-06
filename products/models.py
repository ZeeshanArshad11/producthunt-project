from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    url  = models.URLField(max_length=200)
    body = models.TextField()
    icon = models.ImageField(upload_to = "images/")
    image = models.ImageField(upload_to = "images/")
    # for auto add date and time
    # pub_date = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class Voting(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user','products'))
        index_together = (('user','products'))
