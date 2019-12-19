from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User, Group
from csharp.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'date_added', 'status', 'cost',
                    'customer', 'completion_date', 'manager')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('articul', 'name', 'amount', 'measure_unit', 'purchase_price', 'provider')


class DecorationAdmin(admin.ModelAdmin):
    list_display = ('articul', 'name', 'amount', 'measure_unit', 'purchase_price', 'provider')


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ToolAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        return ((timezone.now() - obj.purchase_date) / 30).days
    time_seconds.admin_order_field = 'purchase_date'
    time_seconds.short_description = 'Время в месяцах'

    list_display = ('name', 'tool_type', 'purchase_date', 'time_seconds', 'amount')

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


admin.site.app_index_template = 'admin/custom_index.html'

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
