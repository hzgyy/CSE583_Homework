#!/bin/bash
mkdir pronto
cd pronto
echo "The Pronto bike dataset provides a detailed historical record of Seattle's short-lived bike-share system, capturing trip durations, station locations, user demographics, and weather conditions." >> README.txt
mkdir data
curl -o data/open_data_year_one.zip https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip data/open_data_year_one.zip -d data/
echo "First 10 lines of 2015_trip_data.csv:"
head data/2015_trip_data.csv
