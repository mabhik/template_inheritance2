from django.shortcuts import render

# Create your views here.
def parent1(request):
    return  render(request,'parent1.html')

def child1(request):
    return render(request,'child1.html')