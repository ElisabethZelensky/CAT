from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from django.contrib.auth.models import User, Group
from csharp.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'date_added', 'status', 'cost',
                    'customer', 'completion_date', 'manager')


class ExpiredIngredientFilter(admin.SimpleListFilter):
    title = 'Годен продукт?'
    parameter_name = 'was_expired'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Да'),
            ('No', 'Нет'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(expired__gt=timezone.now() - datetime.timedelta(days=1))
        elif value == 'No':
            return queryset.exclude(expired__gt=timezone.now() - datetime.timedelta(days=1))
        return queryset


class IngredientAdmin(admin.ModelAdmin):
    def was_expired(self, obj):
        return obj.expired >= timezone.now() - datetime.timedelta(days=1)
    was_expired.boolean = True
    was_expired.short_description = 'Продукт годен?'

    list_display = ('articul', 'name', 'amount', 'measure_unit',
                    'purchase_price', 'was_expired', 'provider')

    list_filter = ('expired', ExpiredIngredientFilter)


class ExpiredDecorationFilter(admin.SimpleListFilter):
    title = 'Годен продукт?'
    parameter_name = 'was_expired'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Да'),
            ('No', 'Нет'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(expired__gt=timezone.now() - datetime.timedelta(days=1))
        elif value == 'No':
            return queryset.exclude(expired__gt=timezone.now() - datetime.timedelta(days=1))
        return queryset


class DecorationAdmin(admin.ModelAdmin):
    def was_expired(self, obj):
        return obj.expired >= timezone.now() - datetime.timedelta(days=1)
    was_expired.boolean = True
    was_expired.short_description = 'Продукт годен?'

    list_display = ('articul', 'name', 'amount', 'measure_unit',
                    'purchase_price', 'expired', 'was_expired', 'provider')

    list_filter = ('expired', ExpiredDecorationFilter)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ToolAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        return ((timezone.now() - obj.purchase_date) / 30).days
    time_seconds.admin_order_field = 'purchase_date'
    time_seconds.short_description = 'Время в месяцах'

    list_display = ('name', 'tool_type', 'purchase_date', 'time_seconds', 'amount')

    list_filter = ('purchase_date', )


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
