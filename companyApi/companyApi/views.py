#function view, we can have class based view as well
from django.http import HttpResponse,JsonResponse


def home_page(request):
    print("home page requested")
    friends=["akshat","kohina"]
    return JsonResponse(friends,safe=False)
    #safe = False -->    
    # return HttpResponse("<h1>this is a home page</h1>")