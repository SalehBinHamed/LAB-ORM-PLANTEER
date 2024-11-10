from django.shortcuts import render
def home_massge(request):

    return render(request , 'main/massge.html')




def contact_views(request):
    return render(request , 'main/contact.html')
    
