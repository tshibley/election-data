import csv
datafile = open('schedule_a-2018-11-06T13_34_34.csv', 'r')
datareader = csv.reader(datafile, delimiter=';')
data = []
camps = dict()

for row in datareader:
    data.append(row)
for d in data:
    d_arr = d[0].split(',')
    key = d_arr[1]
    if key in camps:
        camps[key] += 1
    else:
        camps[key] = 1

d_view = [(v, k) for k, v in camps.iteritems()]
d_view.sort(reverse=True)  # natively sort tuples by first element
for v, k in d_view:
    print "%s: %d" % (k, v)


'''for key, value in camps.items():
    print('campaign: ' + key + ' donation count: ' + str(value))'''


'''

'schedule_a-2018-11-06T13_30_33.csv'

'''
