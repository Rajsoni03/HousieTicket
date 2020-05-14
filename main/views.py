from django.shortcuts import render
import pandas as pd
from random import randint as rnd
from time import time


# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def data(request):
    return render(request, 'main/data.html')


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
        words = {}
        index = []
        word = []
        count = 1
        for i in request.POST:
            if str(i).find('word') == 0:
                word.append(request.POST.get(i, None))
                index.append(count)
                count += 1

        words['Index'] = index
        words['Words'] = word
        data = pd.DataFrame(words, index=None)
        data = pd.DataFrame(
            i + ' - ' + j for i, j in (zip(map(str, (d for d in data['Index'])), map(str, (d for d in data['Words'])))))

        no = 1
        length = data.shape[0] - 1

        finalTicket = []
        for i in range(300):
            finalTicket.append(one_ticket())
            no += 1

    params = {
        'final': finalTicket
    }
    return render(request, 'main/create.html', params)
