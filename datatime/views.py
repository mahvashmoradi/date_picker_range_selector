from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class DatePicker(View):
    # def get(self, request, *arg, **kwargs):
    def get(self, request):
        print(request.GET)
        return render(request, 'data.html')

    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            print(dict(request.POST.items()))  # محتویات درخواست مشاهده کنید
        return JsonResponse({'Hi': 'Hi'})
