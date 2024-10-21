from django.shortcuts import render
from django.views import View

# Create your views here.

# Class based views
class RegistrationView(View):
    # For handling GET request
    def get(self,request):
        return render(request, "authentication/register.html")