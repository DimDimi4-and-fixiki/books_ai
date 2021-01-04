import csv


class CSVWriter(object):
    def __init__(self, path):
        self.fields = ["id", "title", "author", "rating", "tags", "volume", "image", "link"]
        self.filename = path
        with open(self.filename, "w", encoding="utf-8", newline='\n') as csv_file:
            self.writer = csv.DictWriter(csv_file, fieldnames=self.fields)
            self.writer.writeheader()

    def write_row(self, row: list):
        """
        Writes row to the csv file
        :param row:  row in the dictionary
        """
        with open(self.filename, "a+", encoding="utf-8", newline='\n') as csv_file:
            self.writer = csv.writer(csv_file)
            self.writer.writerow(row)

