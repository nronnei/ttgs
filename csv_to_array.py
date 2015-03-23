__author__ = 'Nick Ronnei (nronnei@gmail.com)'
## Written with Python 2.7
## Works very well on my PC
import csv


def readCSV(filepath):
    """

    Reads every line in the csv file and returns
    each line as an item in a list.  Each item is
    a sublist containing the values of each row.

    ex. -->
    return = [["foo", "bar"], ["foo", "bar"]]

    """
    with open(filepath, "r") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        return list(reader)


## END FUNCTIONS
## Declare necessary

## DON'T FORGET: you have to include the file extension (.csv)
in_path = raw_input("The file path to the CSV file:  ")

## DON'T FORGET: you have to include the file extension (.txt)
out_path = raw_input("The file path of the array's text file:  ")

## Just the name of the array, no need for "var" (ex. "parkInfo")
array_name = raw_input("What should we name this array?  ")
start_text = "var " + array_name + " = [\n"
end_text = "];"
csv_in = readCSV(in_path)

## Start the hard work

with open(out_path, "w") as txt:
    txt.write(start_text)
    cutComma = len(csv_in) - 1
    i = 0
    for row in csv_in:
        if i < cutComma:
            text = str(row) + ",\n"
        else:
            text = str(row) + "\n"
        i += 1
        txt.write(text)
    txt.write(end_text)

## End the hard work

print("Array writing successful, you can find it here: " + out_path)
