import csv

class CsvParser:

	def get_rows(self, file_name):
		rows = []
		csvfile = open(file_name, newline='')
		reader = csv.reader(csvfile)
		for row in reader:
			rows.append(row)
		return rows



