filename =["Harry|Potter|Gryffindor|McGonagall|Fall 2015"
"Laura|Madley|Hufflepuff|Sprout|Spring 2016"
]


for line in filename:
    data_lines = line.split("|")
    unique_houses = data_lines[2]
    print unique_houses
