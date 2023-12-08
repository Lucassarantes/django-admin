from django.contrib import admin

from .models import Dog
from .models import Owner, OwnerAdmin

admin.site.register(Dog)
admin.site.register(Owner, OwnerAdmin)