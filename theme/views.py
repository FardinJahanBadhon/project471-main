from django.shortcuts import render,redirect
from .models import Theme

# Create your views here.
def about(request):
    if Theme.objects.filter(user=request.user.username).exists():
        color = Theme.objects.get(user=request.user.username).color
    else:
        color = 'blue'
    return(render, 'about.html', {'color': color})
def theme(request):
    color = request.GET[('color')]

    if color == 'dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme= Theme.objects.get(user=request.user.username)
            user_theme.user=request.user.username
            user_theme.color='gray'
            user_theme.save()

        else:
            user2 = Theme(user=request.user.username, color='gray')
            user2.save()
    elif color == 'light':
        if Theme.objects.filter(user=request.user.username).exists():
            user_theme1= Theme.objects.GET.get(user=request.user.username)
            user_theme1.user=request.user.username
            user_theme1.color='white'
            user_theme1.save()

        else:
            user4 = Theme(user=request.user.username, color='white')
            user4.save()
    return redirect('/')