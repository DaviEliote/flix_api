from django.contrib import admin
from actors.models import Actor
# Register your models here.

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display=('id','name')