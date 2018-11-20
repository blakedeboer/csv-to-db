from csv_parser import CsvParser

def test_csv_parser():
	csv_parser = CsvParser()
	rows = csv_parser.get_rows('sports_data.csv')
	assert 5 == len(rows)