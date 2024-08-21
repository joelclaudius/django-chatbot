from django.http import JsonResponse
from django.shortcuts import render

# views

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = "Hi , this is a simple chatbot. You said: " + message + ". I'm here to join you on the   server and help you. "
        return JsonResponse({'response': response})
    return render(request, 'chatbot.html')
