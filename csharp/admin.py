from django.contrib import admin
from csharp.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'date_added', 'manager')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'measure_unit', 'provider')


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.index_template = 'admin/custom_index.html'

admin.site.site_header = 'Jopa'

admin.site.register(Order, OrderAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Provider, ProviderAdmin)

admin.site.register(Product)
admin.site.register(Decoration)
admin.site.register(DecorationSpecification)
admin.site.register(SemifinishedSpecification)
admin.site.register(ProductSpecification)
admin.site.register(EquipmentType)
admin.site.register(OperationSpecification)
admin.site.register(Equipment)
