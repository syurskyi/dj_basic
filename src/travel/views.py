from django.http import HttpResponse
from django.shortcuts import render

# def home_view(request):
#     name = "Grey"
#     html = """<html> <body>
#     <h1> Hello {}!!! </h1>
#     </body></html""".format(name)
#     return HttpResponse(html)

def home_view(request):
    name = "Grey"
    context = {'name': 'Maja'}
    html = """<html> <body>
    <h1> Hello {}!!! </h1>
    </body></html""".format(name)
    return render(request, 'home.html', context)
