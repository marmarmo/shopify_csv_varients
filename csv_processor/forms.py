from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV")
    product_name = forms.CharField(label="Product Name", max_length=255)
    option1_name = forms.CharField(label="Option 1 Name", max_length=255, required=False)
    option1_values = forms.CharField(label="Option 1 Values (comma-separated)", widget=forms.Textarea, required=False)
    option2_name = forms.CharField(label="Option 2 Name", max_length=255, required=False)
    option2_values = forms.CharField(label="Option 2 Values (comma-separated)", widget=forms.Textarea, required=False)
    option3_name = forms.CharField(label="Option 3 Name", max_length=255, required=False)
    option3_values = forms.CharField(label="Option 3 Values (comma-separated)", widget=forms.Textarea, required=False)
    
    flag_type = forms.CharField(label="Flag Type (e.g., Grouping, Taper, Diameter)", max_length=255, required=False)
