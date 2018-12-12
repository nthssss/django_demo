from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.You're at polls index")

def detail(request,question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    reponse = "You're looking at question %s."
    return HttpResponse(reponse % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting at question %s." % question_id)
