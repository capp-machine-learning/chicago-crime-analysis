# Chicago Crime Analysis

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

All datasets used are downloaded from [Chicago Data Portal](https://data.cityofchicago.org/).
These datasets are not in this repo due to the size of these files.

To download the datasets that I used:

1. Use data_downloader.py in this repo:

        $ cd chicago-crime-analysis/data
        $ python data_downloader.py
        chicago_crime_2017.csv downloaded!
        chicago_crime_2018.csv downloaded!
        All datasets downloaded!

1. If the datasets already exist, you will see:

        $ cd chicago-crime-analysis/data
        $ python data_downloader.py
        chicago_crime_2017.csv already exists!
        chicago_crime_2018.csv already exists!
        All datasets downloaded!
