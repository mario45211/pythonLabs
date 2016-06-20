def avg(dict):
    sum, l = 0, 0
    for i in dict:
        for category, mark in dict[i].items():  # prosciej wybierac klucze slownika dict[i].keys() a pozniej wartosci tych kluczy dict[i][k]
            sum += mark
            l += 1
        if (sum / l < 3):
            print(i, end=' ')
            print(sum / l)
        sum, l = 0, 0


def avgCategorized(dict):
    sum = {}
    for i in dict:
        # for category,mark in dict[i].items():
        for k in dict[i].keys():
            # sum[k]+=dict[k]
            # sum[k[0]]+=1
            if k not in sum:
                sum[k] = {'suma': 0, 'ile': 0}
            sum[k]['suma'] += dict[i][k];
            sum[k]['ile'] += 1
    # print(sum)
    for k in sum.keys():
        print(k, ": ", sum[k]['suma'] / sum[k]['ile'])


dziennik = {"Marek": {"kolokwium 1": 4.0, "egzamin": 3.0},
            "Jan": {"kolokwium 1": 2.0, "egzamin": 2.0},
            "Staś": {"kolokwium 1": 5.0, "egzamin": 2.0, "kolokwium 2": 4.5},
            "Maciuś": {"kolokwium 1": 2.0, "kolokwium 2": 3.5, "odpowiedz przy tablicy smierci": 2.0, "egzamin": 2.0}}

avg(dziennik)

avgCategorized(dziennik)
