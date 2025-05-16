from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .forms import makeform
from django.contrib import messages



def home(request):
    if request.method == 'POST':
            data = makeform(request.POST)
            data.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/contact')
    else:
            data =  makeform()
    return render(request,"index.html",{'form':data})
    # temp = loader.get_template("index.html")
    # return HttpResponse(temp.render())
def about(request):
    temp = loader.get_template("about.html")
    return HttpResponse(temp.render())
def service(request):
    temp = loader.get_template("services.html")
    return HttpResponse(temp.render())
def portfolio(request):
    temp = loader.get_template("portfolio.html")
    return HttpResponse(temp.render())
def contact(request):
        if request.method == 'POST':
            data = makeform(request.POST)
            data.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('/contact')
        else:
            data =  makeform()
        return render(request,"contact.html",{'form':data})
    # temp = loader.get_template("contact.html")
    # return HttpResponse(temp.render())

