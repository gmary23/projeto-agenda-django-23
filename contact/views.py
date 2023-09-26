from django.shortcuts import render

# Geila - Criado uma view - aqui diz o que precisa renderizar
# Essa view precisa está ligada a uma url
def index(request):
    return render(
        request,
        'contact/index.html',
    )

