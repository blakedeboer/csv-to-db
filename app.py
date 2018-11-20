
from csv_parser import CsvParser
from database import save_rows

CSV_FILE_NAME = "sports_data_2.csv"

def run():
	csv_parser = CsvParser(CSV_FILE_NAME)
	header = csv_parser.get_header()
	print(header)
	rows = csv_parser.get_rows()
	save_rows(header, rows)

run()