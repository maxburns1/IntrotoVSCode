from django.contrib import admin

# Register your models here.
from .models import Topic, Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'short_text', 'date_added')

    # This function takes the 'obj' (the specific Entry) and 
    # returns the shortened version from your models.py
    def short_text(self, obj):
        return str(obj) 

    # This tells Django what to put at the top of the column
    short_text.short_description = 'Text'

admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)