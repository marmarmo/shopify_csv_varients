from django.shortcuts import render
from .forms import CSVUploadForm

def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the CSV file here
            return render(request, "csv_processor/upload_success.html")  # Placeholder for now
    else:
        form = CSVUploadForm()

    return render(request, "csv_processor/upload.html", {"form": form})
