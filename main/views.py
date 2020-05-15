from django.shortcuts import render
import pandas as pd
from random import randint as rnd
from time import time
from .models import List, Word


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def data(request):
    params = {
        'list': List.objects.all().order_by('-date')
    }
    return render(request, 'main/data.html', params)


def create(request):
    finalTicket = 0

    def one_ticket():
        ticket = []
        for i in range(3):
            r1 = [data.iloc[rnd(0, length), 0], data.iloc[rnd(0, length), 0], data.iloc[rnd(0, length), 0],
                  data.iloc[rnd(0, length), 0], data.iloc[rnd(0, length), 0]]
            ticket.append(r1)
        return ticket

    if request.method == 'POST':
        words, index, word = {}, [], []
        count = 1
        name = 'List{}'.format(int(time())) if request.POST.get('listname', None) is None else request.POST.get('listname', None)
        if 'save' in request.POST:
            List(list_name=name, footer=request.POST.get('footerline', None)).save()
            list_obj = List.objects.filter(list_name=name)[0]

        for i in request.POST:
            if str(i).find('word') == 0:
                word.append(request.POST.get(i, None))
                index.append(count)
                if 'save' in request.POST:
                    Word(list_id=list_obj.id, word=request.POST.get(i, None)).save()
                count += 1

        if 'save' in request.POST:
            list_obj.total_words = len(word)
            list_obj.save()

        words['Index'] = index
        words['Words'] = word
        data = pd.DataFrame(words, index=None)
        data = pd.DataFrame(
            i + ' - ' + j for i, j in (zip(map(str, (d for d in data['Index'])), map(str, (d for d in data['Words'])))))
        no = 1
        length = data.shape[0] - 1

        finalTicket = []
        noticket = int(request.POST.get('noticket', 1))
        for i in range(noticket):
            finalTicket.append(one_ticket())
            no += 1

    footer = (List.objects.all().order_by('-date')[0]).footer
    print(footer)
    params = {
        'final': finalTicket,
        'footerline': footer
    }
    return render(request, 'main/create.html', params)
