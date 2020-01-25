from .models import *
from django import forms


class DecorationForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = '__all__'

    def clean(self):
        amount = self.cleaned_data['amount']
        purchase_price = self.cleaned_data['purchase_price']
        weight = self.cleaned_data['weight']
        if amount < 0:
            raise forms.ValidationError("Количество не может быть отрицательным")
        if purchase_price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        if weight < 0:
            raise forms.ValidationError("Вес не может быть отрицательным")
        return self.cleaned_data


class DecorationSpecificationForm(forms.ModelForm):
    class Meta:
        model = DecorationSpecification
        fields = '__all__'

    def clean(self):
        decoration_amount = Decoration.objects.get(name=self.cleaned_data['decoration']).amount
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise forms.ValidationError("Количество не может быть отрицательным")
        if amount > decoration_amount:
            raise forms.ValidationError("Недостаточно украшений на складе")
        return self.cleaned_data


class DecorationSpecificationFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            decoration_amount = Decoration.objects.get(name=form.cleaned_data['decoration']).amount
            amount = form.cleaned_data['amount']
            if amount < 0:
                raise forms.ValidationError("Количество не может быть отрицательным")
            if amount > decoration_amount:
                raise forms.ValidationError("Недостаточно украшений на складе")
        return self.cleaned_data


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

    def clean(self):
        amount = self.cleaned_data['amount']
        purchase_price = self.cleaned_data['purchase_price']
        if amount < 0:
            raise forms.ValidationError("Количество не может быть отрицательным")
        if purchase_price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return self.cleaned_data


class ProductSpecificationFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            product_amount = Ingredient.objects.get(name=form.cleaned_data['ingredient']).amount
            amount = form.cleaned_data['amount']
            if amount < 0:
                raise forms.ValidationError("Количество не может быть отрицательным")
            if amount > product_amount:
                raise forms.ValidationError("Недостаточно ингредиентов на складе")
        return self.cleaned_data


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = '__all__'

    def clean(self):
        amount = self.cleaned_data['amount']
        if amount < 0:
            raise forms.ValidationError("Количество не может быть отрицательным")
        return self.cleaned_data
