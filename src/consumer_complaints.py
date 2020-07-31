import csv

'''
________________________Open file and create a 2D list data set____________________
'''

with open('input/complaints.csv') as file:
    reader = csv.reader(file)
    dataset = []
    for line in reader:
        row = ['20' + line[0][-2:], line[1], line[7]]
        dataset.append(row)

dataset = dataset[1:]

'''
_______Index_______
 0 - Date received
 1 - Product
 2 - Company

__________________________Reorganize data set into nested dictionaries__________________
'''


def create_dictionary(dataset):
    # Calculates the first metric of the problem:
    # Total number of complaints received for that product that year

    unique_pairs = {}

    for row in dataset:
        pair = row[1] + ',' + row[0]  # 'product, year' pair
        comp = row[2]
        if pair not in unique_pairs:
            unique_pairs.update({pair: {comp: 1}})  # create new pair & company entry, start tally
        elif comp not in unique_pairs[pair]:
            unique_pairs[pair].update({comp: 1})  # create new company entry, start tally
        else:
            unique_pairs[pair][comp] += 1  # update tally for company

    return unique_pairs


output = create_dictionary(dataset)

'''
 ______Stats/unique pair______
 1 = sum(tallies)
 2 = len(companies)
 3 = max(tallies)/sum(tallies)

_________________________Calculate stats & print output__________________________
'''

with open('output/report.csv', 'w', newline='') as file:
    output_writer = csv.writer(file)

    for pair in sorted(output.keys()):
        stat_1 = 0
        stat_2 = len(output[pair])
        max_tally = 0

        for company in output[pair]:
            stat_1 += output[pair][company]
            if output[pair][company] > max_tally:
                max_tally = output[pair][company]

        stat_3 = round(max_tally * 100 / stat_1)

        output_writer.writerow([pair[:-5], pair[-4:], str(stat_1), str(stat_2), str(stat_3)])
