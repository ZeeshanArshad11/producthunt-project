from django.contrib import admin
from .models import Product, Voting

# Register your models here.
admin.site.register(Product)

#admin.site.register(Voting)
@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    list_display = ['products','user']
    list_filter = ['products','user']
