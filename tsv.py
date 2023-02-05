import csv
with open("C:/Users/hp/Documents/lang.tsv",'r+') as file:
    # Making all columns a single word and checking if any non alpha numeric character presnt.
    first_line = file.readline().strip().replace("\t","")
    #Checking if the header present.
    for _ in first_line:
        if (_.isalpha()) :#Considering that heaader can have only A-Z and a-z character No digits,punctuation,underscore etc.
                headers_present = False
        else:
            headers_present = True  
            break #Even if once the headers_present is True break the loop.
    # Going back to the first line of open file.
    file.seek(0)
    tsv_file = csv.reader(file, delimiter="\t")
    arr = []
    # Getting the values of last column.
    for line in tsv_file:
        x = len(line) # Finding the length of line
        if(x==0): # If the line is empty then skipping the line by continue keyword.
            continue
        arr.append(line[x-1]) # Extracting the last column values of every line.
    # Sorting and Printing the values of last column and Removing the header if present.
    if(headers_present):
        x = arr.pop(0)
        sorted = sorted(arr)
        print(sorted)
    else:
        sorted = sorted(arr)
        print(sorted)
