from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world.")

def hello_name(request, question_id):
    return HttpResponse("Hello, {}".format(question_id))