import csv
import itertools

import matplotlib.pyplot as plt

from record import Record


# here you change number of column in array in type of Record to change variable x
# 0 - people
# 1 - groups
# 2 - percentage

def filter_columns(postgres, neo, column):
    return filter_data(postgres, 1, column), filter_data(neo, 1, column)

# this functions extract data for each step

def load_employees(postgres, neo):
    return extract_columns(filter_columns(postgres, neo, 4))


def load_contacts(postgres, neo):
    return extract_columns(filter_columns(postgres, neo, 5))


def parameters(postgres, neo):
    return extract_columns(filter_columns(postgres, neo, 6))


def simulation(postgres, neo):
    return extract_columns(filter_columns(postgres, neo, 7))

# util functions

def extract_columns(data):
    x_list = [x[0] for x in data[0]]
    y1_list = [y[1] for y in data[0]]
    y2_list = [y[1] for y in data[1]]
    return x_list, y1_list, y2_list


def extract(record, c1, c2):
    return record.fields[c1], record.fields[c2]


def filter_data(result_list, column1, column2):
    return [extract(x, column1, column2) for x in result_list]

# plot drawing

def run_plot(data, title, label):
    fig = plt.figure()
    plt.plot(data[0], data[1], 'b', label='PostgreSQL')
    plt.plot(data[0], data[2], 'r', label='Neo4j')
    plt.xlabel(label)
    plt.ylabel('Time [ms]')
    plt.title(title)
    plt.legend()
    return fig

# split data

def extract_result_data():
    postgres_data = []
    neo_data = []
    with open('results/result_times.csv') as f:
        lines = itertools.islice(f, 1, None)
        plots = sorted(csv.reader(lines), key=lambda x: int(x[1]))

        for row in plots:
            record = Record()
            record.add_result(row)
            if row[0] == "postgres":
                postgres_data.append(record)
            else:
                neo_data.append(record)
    return postgres_data, neo_data
