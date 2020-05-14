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
    finalTicket = [[[]]]
    def one_ticket():
        ticket = []
        # ticket.append([no])
        for i in range(3):
            r1 = [data.iloc[rnd(0, length), 0], data.iloc[rnd(0, length), 0], data.iloc[rnd(0, length), 0],data.iloc[rnd(0, length), 0], data.iloc[rnd(0, length), 0]]
            ticket.append(r1)
        # ticket.append([])
        # ticket.append(["दि जैन सोशल ग्रुप जबलपुर मेन"])
        # ticket.append(["अध्यक्ष. गोपाल अर्चना,  सचिव .प्रशांत प्रियांशी,  सांस्कृतिक प्रभारी- कपिल मोनिका,"])
        # ticket.append(
        #     ["सांस्कृतिक प्रभारी - नवीन मनीषा,  विशेष सहयोगी - मिलिंद मौली, सांस्कृतिक प्रभारी - नवीन मनीषा,  "
        #      "विशेष सहयोगी - मिलिंद मौली"])
        # ticket.append([])
        # ticket.append([])
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
                count+=1

        words['Index'] = index
        words['Words'] = word
        # print(words)

        data = pd.DataFrame(words, index=None)
        data = pd.DataFrame(
            i + ' - ' + j for i, j in (zip(map(str, (d for d in data['Index'])), map(str, (d for d in data['Words'])))))
        # print(data)

        no = 1
        length = data.shape[0] - 1

        finalTicket = []
        for i in range(300):
            finalTicket.append(one_ticket())
            no += 1

    params = {
        'final' : finalTicket
    }
    return render(request, 'main/create.html', params)
