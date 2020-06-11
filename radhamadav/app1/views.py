from django. shortcuts import HttpResponse,render
def sirsilla(request):
    return render(request,'cloth.html')
