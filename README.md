# Divrods Project Data Analysis

The goal of this project is to process, analyze and create a recommendatione engine for artwork hosted by the Minneapolis Institute of Arts. This repository includes raw data, scripts used to reorganize and wrangle the data, and Juypter notebooks used in visualization and model development. More information about the Divrods project and methods to gather data can be found here: https://miaarttech2016.wordpress.com/2017/

## Getting Started

All scripts for this project are written using Python 3.6.7. After cloning this repository, the packages for this project can be downloaded using the requirements.txt file:
```
pip install -r requirements.txt
```
Juypter Notebooks can be installed and accessed through Anaconda. More information on installation can be found here: https://jupyter.org/install

## Workflow

The data for this project was stored in three locations - a .csv file with user preference data, a .csv file with artwork information, and a JSON file with device logger information. The first part of this project was to merge all data sets together. This was done with two scripts, 'json_to_csv.py', which converted the JSON file into a .csv format using the default Python csv library, and 'import_art_data.py', which used the request library to grab data from the Minneapolis Institute of Art's elasticsearch API. The 'import_art_data' script appends certain fields from the request response to the 'artwork_data' csv using pandas, then writes the data to the 'extended_artwork_data' file. In addition, a Juypter Notebook titled 'data_merge_and_reforma't examined the device logger and preferences csv's, then merged appropriate fields together to create the 'merged_preferences.csv'.

After the data was merged, it was analyzed through the 'data analysis' Juypter notebook. This notebook provides insights on the peak times when responses were submitted, the overall preferences of the participants, and the preferences trends among mediums and historical periods. Once this analysis was complete, the data was used to create recommendation engines using Singular Value Decomposition and K-Nearest Neighbor models in the 'Recommender models' Notebook. The Surprise scikit package was used for model training and testing. More details on the results can be found in that Notebook.
