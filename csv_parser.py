import csv

class CsvParser:
	def __init__(self, file_name):
		self._rows_with_header = self._get_rows_with_header(file_name)

	def _get_rows_with_header(self, file_name):
		rows = []
		csvfile = open(file_name, newline='')
		reader = csv.reader(csvfile)
		for row in reader:
			rows.append(row)
		return rows

	def get_header(self):
		return self._rows_with_header[0]

	def get_rows(self):
		return self._rows_with_header[1::]



