from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
def app(request):
    return render(request, 'app.html')
def gameOver(request):
    return render(request, 'game_over.html')
def dynamic_image(request, image_name):
    # Lógica para carregar a imagem dinamicamente
    img = Image.open(request + image_name)
    
    # Lógica para processar a imagem, se necessário
    
    # Retorna a imagem como uma resposta HTTP
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response