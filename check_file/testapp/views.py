from django.shortcuts import render
from .models import FileCheck
from django.shortcuts import redirect
import os

def page(request):
    #очистим папку с файлами и базу данных
    FileCheck.objects.all().delete()

    if "text" not in str(os.getcwd()):
        if "files" not in str(os.getcwd()):
            os.chdir('files/text')
        else:
            os.chdir('text')
    for file in os.listdir():
        os.remove(os.path.join(os.getcwd(), file))


    if request.POST:
        FileCheck.objects.create(file=request.FILES.get('file'))
        return redirect("check")
    else:
        return render(request, "start.html")

def check(request):
    words = None
    words_amount = {}
    response = ""
    filename = FileCheck.objects.latest('id')
    if 'text' in str(os.getcwd()):
        os.chdir('../')
    with open(f"{filename.file.name}") as file:
        text = file.read()

    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
    text = text.lower()  # убираем верхний регистр
    words = text.split()
    if request.POST:
        our_word = request.POST.get('text')


        if our_word in words_amount:
            response = 'Вы уже искали это слово'
        else:
            if our_word not in words:
                response = 'Такого слова нет в тексте. Попробуйте другое слово'
            else:
                for word in words:
                    if word == our_word:
                        if our_word in words_amount:
                            words_amount[word] = words_amount[word]+1
                        else:
                            words_amount[word] = 1
                response = f'Слово "{our_word}" встречается в файле {words_amount[our_word]} раз'

    context = {
        "last" : FileCheck.objects.latest('id'),
        "response" : response
    }
    print(f'words_amoun после===:{words_amount}')

    return render(request, "check.html", context)
