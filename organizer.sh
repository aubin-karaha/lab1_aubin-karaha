#!/bin/bash

# This script was made to make sure there is a folder called "archive" to keep old files in after running the program.

# Checking for an available archive

if [ ! -d "archive" ]; then
	mkdir archive
	echo "Created an archive directory."
fi

timestamp=$(date +"%Y%m%d-%H%M%S")

# Checking whether grades.csv file is in the current directory

if [ ! -f "grade.csv" ]; then
	echo "Error: grades.csv file was not found in the current directory"
	exit 1
fi

# Renaming and moving grades.csv into an archive folder then creating a new one

new_filename="grades_$timestamp.csv"
mv grades.csv "archive/$new_filename"

touch grades.csv

echo "$timestamp --- original file: grades.csv --- archived as: archive/$new_filename" >> organizer.log

echo "Archiving complete."
echo "Original file moved to: archive/$new_filename"
echo "Details logged in organizer.log"
