from django.shortcuts import render
from django.views import View


# Create your views here.

class CoreView(View):

    @staticmethod
    def get(request):
        return render(request,"core/index.html")
