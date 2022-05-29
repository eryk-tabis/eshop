from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        # add to field`s class given property
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'

    class Meta:
        """
        Properties for Order form
        """
        model = Order
        fields = ['first_name', 'last_name', 'email']
        required_fields = ['first_name', 'last_name', 'email']
