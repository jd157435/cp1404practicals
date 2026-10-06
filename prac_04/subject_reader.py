"""
CP1404/CP5632 Practical
Data file -> lists program
"""
from typing import Any

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subjects = load_data(FILENAME)
    print_subject_details(subjects)


def print_subject_details(subjects: list[Any]):
    name_width = max(len(subject[1]) for subject in subjects)
    number_of_students_width = max(len(str(subject[2])) for subject in subjects)
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:{name_width}} and has {subject[2]:{number_of_students_width}}")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subjects = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        subjects.append([parts[0], parts[1], int(parts[2])])
        # print(data)  # See if that worked
        # print("----------")
    input_file.close()
    return subjects


main()
