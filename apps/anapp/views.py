from django.shortcuts import render
from .forms import ContactForm
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'anapp/index.html', {})


# FBV
# def contactPage(request):
#     form = ContactForm()
#     return render(request, "anapp/contact.html", {"form": form})


def contact(request):
    form = ContactForm()
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({"success": True}, status=200)
    # return JsonResponse({"success": False}, status=400)
    return render(request, "anapp/contact.html", {"form": form})
