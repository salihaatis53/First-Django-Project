from django.shortcuts import render, HttpResponse

# Create Saliha Atiþ
def anasayfa(request):
    if request.user.is_authenticated():
        context = {
            'isim': 'Umut',
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    return render(request, 'home.html', context)
