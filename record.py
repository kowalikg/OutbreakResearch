class Record:
    def __init__(self):
        self.fields = []

    def add_result(self, row_values):
        self.fields.append(int(row_values[1]))
        self.fields.append(int(row_values[2]))
        self.fields.append(int(row_values[3]))
        self.fields.append(int(row_values[4]))
        self.fields.append(int(row_values[5]))
        self.fields.append(int(row_values[6]))
        self.fields.append(int(row_values[7]))
        self.fields.append(int(row_values[8]))

