from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Use one of the other routes")
def system(request):
    return HttpResponse("My favorite OS is Windows")
def language(request):
    return HttpResponse("My favorite language is JavaScript")
def ide(request):
    return HttpResponse("My favorite IDE is currently IntelliJ")