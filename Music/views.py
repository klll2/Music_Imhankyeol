from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from Music.models import Music

def list_musics(request):
    musics = Music.objects.all()
    return render(request, 'usermgmt/list_musics.html', {'musics' : musics})
    # instead of get_template()


from Music.forms import MusicForm


def create_music(request):
    form = MusicForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_musics')

    return render(request, 'usermgmt/music_form.html', {'form': form})


def update_music(request, id):
    music = Music.objects.get(id=id)
    form = MusicForm(request.POST or None, instance=music)

    if form.is_valid():
        form.save()
        return redirect('list_musics')

    return render(request, 'usermgmt/music_form.html', {'form': form, 'music': music})


def delete_music(request, id):
    music = Music.objects.get(id=id)

    if request.method == 'POST':
        music.delete()
        return redirect('list_musics')

    return render(request, 'usermgmt/music_delete_confirm.html', {'music': music})

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index/home.html')

def author(request):
    return render(request, 'index/author.html')