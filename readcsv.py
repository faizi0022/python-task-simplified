import csv
with open("name1.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\n')
    line_count = 0
    lines = []
    for row in csv_reader:
        # print(row)
        # print(type(row))
        lines.append(row[0])
        line_count += 1
    print(f'Processed {line_count} lines.')
    lines=sorted(lines)

    # with open("newcsv.csv",mode='w') as write_file:
    #     for line in lines:
    #         print(line)
    #         write_file.write(line)
    #         write_file.write('\n')

    with open("newcsv.csv",mode='w',newline='') as write_file:
        writer = csv.writer(write_file)
        for line in lines:
            # print(line)
            writer.writerow([line])
        


    word_count=0
    character_length=0
    for line in lines:
        words=line.split()
        word_count+=len(words)
        for word in words:
            character_length+=len(word)
    print(word_count)
    print(character_length)
    print(f'Average word length is: {character_length/word_count}')
