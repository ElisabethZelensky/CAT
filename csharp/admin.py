from django.contrib import admin
from csharp.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'date_added', 'manager')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('articul', 'name', 'amount', 'measure_unit', 'purchase_price', 'provider')


class DecorationAdmin(admin.ModelAdmin):
    list_display = ('articul', 'name', 'amount', 'measure_unit', 'purchase_price', 'provider')


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'tool_type', 'purchase_date', 'amount')

    list_filter = ['purchase_date']

class OperationSpecificationInline(admin.StackedInline):
    model = OperationSpecification
    extra = 1


class DecorationSpecificationInline(admin.StackedInline):
    model = DecorationSpecification
    extra = 1


class ProductSpecificationInline(admin.StackedInline):
    model = ProductSpecification
    extra = 1


class SemifinishedSpecificationInline(admin.StackedInline):
    model = SemifinishedSpecification
    extra = 1
    fk_name = "product"

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [SemifinishedSpecificationInline, ProductSpecificationInline,
               DecorationSpecificationInline, OperationSpecificationInline]
#     def get_fieldsets(self, request, obj=None):
#         fieldsets = super(OperationSpecificationAdmin, self).get_fieldsets(request, obj)
#         fieldsets[0][1]['fields'] += ['num']
#         fieldsets[0][1]['fields'] += ['equipment_type']
#         fieldsets[0][1]['fields'] += ['operation_time']
#         return fieldsets


admin.site.index_template = 'admin/custom_index.html'

admin.site.site_header = 'Jopa'

admin.site.register(Order, OrderAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Provider, ProviderAdmin)

admin.site.register(Product, ProductAdmin)
admin.site.register(Decoration, DecorationAdmin)
admin.site.register(DecorationSpecification)
admin.site.register(SemifinishedSpecification)
admin.site.register(ProductSpecification)
admin.site.register(EquipmentType)
admin.site.register(OperationSpecification)
admin.site.register(Equipment)

admin.site.register(Tool, ToolAdmin)
