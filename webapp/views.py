from django.shortcuts import render



def index(requests):
    return render(requests, 'webapp/index.html')



def about(requests):
    return render(requests, 'webapp/about.html')

def contact(requests):
    return render(requests, 'webapp/contact.html')

def services(requests):
    return render(requests, 'webapp/services.html')

def portfolio(requests):
    return render(requests, 'webapp/portfolio-item.html')
