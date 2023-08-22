



# from django import forms
# from django.core.exceptions import ValidationError

# class AlphanumericMinLengthField(forms.CharField):
#     def __init__(self, min_length=None, *args, **kwargs):
#         self.min_length = min_length
#         super().__init__(*args, **kwargs)
    
#     def validate(self, value):
#         super().validate(value)
#         if not value.isalum():
#             raise ValidationError("This field must contain only alphanumeric characters. ")
#         if self.min_length is not None and len(value)<self.min_length:
#             raise ValidationError(f"This field must be atleast {self.min_length} characters long.")
        
#     # from .fields import AlphanumericMinLengthField

# class CustomForm(forms.Form):
#     alphanumeric_field = AlphanumericMinLengthField(min_length=5, required=True, label="Alphanumeric Field")



