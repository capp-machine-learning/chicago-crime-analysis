import csv
import requests
import os

crime_2017_url = "https://data.cityofchicago.org/api/views/d62x-nvdr/rows.csv?accessType=DOWNLOAD"
crime_2018_url = "https://data.cityofchicago.org/api/views/3i3m-jwuy/rows.csv?accessType=DOWNLOAD"
crime_2017_filename = "chicago_crime_2017.csv"
crime_2018_filename = "chicago_crime_2018.csv"
crime_url_filename = [
    (crime_2017_url, crime_2017_filename),
    (crime_2018_url, crime_2018_filename)
    ]

def download_dataset(url_filename_tuple):

    for data_url, filename in url_filename_tuple:

        if os.path.isfile(filename):
            print("{} already exists!".format(filename))

        else:
            data = requests.get(data_url, stream=True)

            with open(filename, 'w') as f:
                writer = csv.writer(f)
                reader = csv.reader(data.text.splitlines())
                for row in reader:
                    writer.writerow(row)

            print("{} downloaded!".format(filename))
    
    print("All datasets downloaded!")

if __name__ == "__main__":
    download_dataset(crime_url_filename)
