from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.base import ContentFile
from io import BytesIO
from .models import Word
from PIL import Image, ImageOps
from random import randint, shuffle, randrange
from .forms import WordForm
from django.utils import timezone
# import pyautogui
import os
path = os.getcwd()

def convert_word(word):
    # width, height = pyautogui.size()
    global bg_color
    rand = randint(0,1)
    if rand == 0:
        bg = Image.new('L', (1920, 1080), "WHITE")
        bg_color = "w"
    elif rand == 1:
        bg = Image.new('L', (1920, 1080), "BLACK")
        bg_color = "b"

    f_imgs = [] # [[img_x, img_y, size], ...]

    word = list(word)
    shuffle(word)
    for alpha in word:
        if alpha.isdigit() == True:
            # Use following path for pythonanywhere env
            # alpha_img = Image.open(path + '/typeyourwords/project0/static/alphas/' + alpha + '.png')
            alpha_img = Image.open(path + '/project0/static/alphas/' + alpha + '.png')
        elif alpha == " ":
            rand = randint(0,1)
            if rand == 0:
                # alpha_img = Image.open(path + '/typeyourwords/project0/static/alphas/space.png')
                alpha_img = Image.open(path + '/project0/static/alphas/space.png')
            else:
                # alpha_img = Image.open(path + '/typeyourwords/project0/static/alphas/space_invert.png')
                alpha_img = Image.open(path + '/project0/static/alphas/space_invert.png')
        else:
            alpha = alpha.lower()
            # Open the alphabet image
            rand = randint(0,1)
            if rand == 0:
                # alpha_img = Image.open(path + '/typeyourwords/project0/static/alphas/' + alpha + '.png')
                alpha_img = Image.open(path + '/project0/static/alphas/' + alpha + '.png')
            else:
                # alpha_img = Image.open(path + '/typeyourwords/project0/static/alphas/' + alpha + ' invert.png')
                alpha_img = Image.open(path + '/project0/static/alphas/' + alpha + '_invert.png')
        
        # Fix the upper left corner of the image
        arranged = False
        while not arranged:
            img_x = randint(0,bg.size[0]-1)
            img_y = randint(0,bg.size[1]-1)
            arranged = True
            for f in f_imgs:
                if (f[0] == img_x and f[1] == img_y) or (f[0] < img_x < f[0]+f[2] and f[1] < img_y < f[1]+f[2]):
                    arranged = False
                    break
                
        # Find the max size of the image
        h = []
        v = []
        for f in f_imgs:
            if f[0] > img_x and f[1]+f[2] > img_y:
                h.append(f[0]-img_x)
            if f[1] > img_y and f[0]+f[2] > img_x:
                v.append(f[1]-img_y)

        window_range = min(bg.size[0]-img_x, bg.size[1]-img_y)
        if len(h) != 0 and len(v) != 0:
            max_size = min(min(h), min(v), window_range)
        elif len(h) != 0:
            max_size = min(min(h), window_range)
        elif len(v) != 0:
            max_size = min(min(v), window_range)
        else:
            max_size = window_range

        # Resize and paste the image into the background
        size = randint(1, max_size)
        alpha_img = alpha_img.resize((size, size))
        bg.paste(alpha_img, ((img_x, img_y)))
        f_imgs.append([img_x, img_y, size])
    
    img_io = BytesIO()
    bg.save(img_io, format='PNG')
    img_content = ContentFile(img_io.getvalue())
    return img_content

def input_bar(request):
    # if the user submit the input
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            img_content = convert_word(form.cleaned_data['word'])
            word = form.save()
            if bg_color == "w":
                word.is_bg_w = True
            elif bg_color == "b":
                word.is_bg_w = False
            word.image.save(str(word.pk)+'.png', img_content)
            word.created_date = timezone.now()
            word.save()
            return redirect('output_image', pk=word.pk)
    else:
        form = WordForm()
    return render(request, 'project0/input_bar.html', {'form': form})

def output_image(request, pk):
    word = get_object_or_404(Word, pk=pk)
    return render(request, 'project0/output_image.html', {'word':word})

def output_list(request):
    words = Word.objects.all().order_by('-created_date')
    return render(request, 'project0/archive.html', {'words': words})

def about_page(request):
    return render(request, 'project0/about.html')