import csv
import requests

def download_dataset(data_url, filename):

    data = requests.get(data_url, stream=True)

    with open(filename, 'w') as f:
        writer = csv.writer(f)
        reader = csv.reader(data.text.splitlines())
        for row in reader:
            writer.writerow(row)
