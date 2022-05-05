from django.contrib import admin

#furan / furan1234
# Register your models here.
from .models import *

admin.site.register(Producto)
admin.site.register(Remedio)
admin.site.register(CategoriaRemedio)
admin.site.register(MarcaRemedio)