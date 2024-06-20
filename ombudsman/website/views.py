# myapp/views.py
from django.shortcuts import render, redirect
from .forms import MyModelForm

def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form data saved successfully")
            return redirect('success')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = MyModelForm()
    return render(request, 'my_template.html', {'form': form})
