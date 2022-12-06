marker_length = 14
letter_buffer = set()

for line in open("./day6/input","r"):
    line_formatted = line.strip()
    line_chunks = list(line)
    for index in range(marker_length,len(line_chunks) - marker_length) :
        if len(set(line_chunks[index: index+marker_length])) == marker_length:
            # print index AFTER last character, not first
            print(index + marker_length)
            break
        
