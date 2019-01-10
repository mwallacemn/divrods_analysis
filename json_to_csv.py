import json
import csv
import sys
import os
from pathlib import Path

def main(argv):
	cwd = Path(os.getcwd())
	json_file = cwd / argv[0]
	csv_file = cwd / argv[1]
	with open(json_file) as f:
		file = json.load(f)
		with open(csv_file, 'w', newline='') as csvfile:
			csv_writer = csv.writer(csvfile, delimiter=',')
			# grabbing column names
			csv_writer.writerow(['session_id'] + list(file[next(iter(file))][0].keys()))

			for k, v in file.items():
				for row in v:
					csv_writer.writerow([k] + list(row.values()))


if __name__ == "__main__":
	main(sys.argv[1:])