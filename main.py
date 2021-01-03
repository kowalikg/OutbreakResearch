import os
import subprocess

import utils

print("Outbreak 2021")
# write numbers here
employees = [100]
# write numbers here
percentages = [50]
# write numbers here
employees_per_groups = [5, 8, 10, 13, 15, 17, 20, 22, 25]

source_directory = "source"
data_set = 1

# write here path to compiled data generator
generator_path = "OutbreakDataGenerator.jar"

# write here path to compiled calculator
calculator_path = "OutbreakCalculator.jar"

# write here path to database properties
properties_path = "databases.properties"

# data generation

for worker in employees:
    for percentage in percentages:
        for workers_per_group in employees_per_groups:
            print("Launching for {} employees, {} employees per group, {} percentage of infections".format(
                worker, workers_per_group, percentage))
            launch_path = "java -jar {} {} {} {} 100 y {}/{}" \
                .format(generator_path, worker, workers_per_group, percentage, source_directory, data_set)
            subprocess.call(launch_path)  # , stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
            data_set = data_set + 1

directories = sorted(os.listdir(source_directory), key=lambda x: int(x))

# calculation

for subdir in directories:
    dir_path = "{}\\{}".format(source_directory, subdir)
    fileNames = ' '.join([entry.path for entry in os.scandir(dir_path)])
    path = "java -jar {} {} {} 1 results".format(calculator_path, properties_path, fileNames)
    print("Simulation on files {}".format(fileNames))
    subprocess.call(path)

postgresData, neoData = utils.extract_result_data()

# here you run plots for each step

utils.run_plot(utils.load_employees(postgresData, neoData),
               "Title here",
               "Description of x variable").savefig("1.png")
utils.run_plot(utils.load_contacts(postgresData, neoData),
               "Title here",
               "Description of x variable").savefig("2.png")
utils.run_plot(utils.parameters(postgresData, neoData),
               "Title here",
               "Description of x variable").savefig("3.png")
utils.run_plot(utils.simulation(postgresData, neoData),
               "Title here",
               "Description of x variable").savefig("4.png")
