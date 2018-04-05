from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def image_upload_view(request):
    profile = Profile.objects.all()
    if request.POST:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('withcrop:img_uploader')
        return render(request, "create.html", context={"form": form})
    form = ProfileForm()
    return render(request, "create.html", context={"form": form, "profile_list": profile})
