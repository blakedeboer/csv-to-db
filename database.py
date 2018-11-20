import os
import sqlite3

def save_rows(header, rows):
	file_name = 'example2.db'

	if os.path.exists(file_name):
		os.remove(file_name)

	f = open(file_name, 'w+')
	f.close()

	conn = sqlite3.connect(file_name)

	c = conn.cursor()

	column_1 = 'Question text'
	t = 'Question text', 'Response_Type text', 'Choices text'
	# c.execute(f"CREATE TABLE answers (Question text, Response_Type text, Choices text)"
	header_tuple = tuple(header)
	c.execute(f"CREATE TABLE answers {header_tuple}")

	# print(rows)

	for row in rows:
		row_tuple = tuple(row)
		# c.execute("INSERT INTO answers VALUES ('Who is your favorite team?','self','[\"Bears\", \"Packers\", \"Vikings\", \"Lions\"]')")
		c.execute(f"INSERT INTO answers VALUES {row_tuple}")

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()
