from django.shortcuts import render
from django.http import HttpResponse
from .models import Order

def index(request):
    latest_question_list = Order.objects.order_by('-completion_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'csharp/index.html', context)
