# Chicago Crime Analysis

## Getting Started

I used conda as the environment manager.

### Prerequisites

1. Clone the repository.

        $ git clone https://github.com/capp-machine-learning/chicago-crime-analysis.git
        $ cd chicago-crime-analysis

1. A yml file of the environment is available in environment.yml.

        $ conda env create --file=environment.yml
        $ conda activate cca

All datasets used are downloaded from [Chicago Data Portal](https://data.cityofchicago.org/).

To download the datasets that I used:

1. Go to Chicago Data Portal to download the data.

1. Alternatively, you can simply download directly from the url below:

        $ cd data
        $ curl -O https://data.cityofchicago.org/api/views/d62x-nvdr/rows.csv?accessType=DOWNLOAD > chicago_crime_2017.csv
        $ curl -O https://data.cityofchicago.org/api/views/3i3m-jwuy/rows.csv?accessType=DOWNLOAD > chicago_crime_2018.csv
        
### Files

        chicago-crime-analysis
        ├── chicago_crime_data.ipynb
        ├── chicago_crime_data.pdf
        ├── ml_functions.py
        ├── README.md
        └── environment.yml

- __chicago_crime_data.ipynb__: This file is *the main file with all write-up and the bulk of the coding.* Just in case, the code does not run, I have also uploaded a pdf file of the same write-up with all outputs.
- __ml_functions.py__: This python file has a collection of functions that I have written for this analysis. All functions are imported and used in __chicago_crime_data.ipynb__.
