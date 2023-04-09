def find_missing_letter(chars):
    missChar = ''
    for i in range(0,len(chars)-1):
        if(ord(chars[i+1]) - ord(chars[i]) > 1):
            missChar = chr(ord(chars[i])+1)

    return missChar

print(find_missing_letter(["a","b","c","d","f"]))
print(find_missing_letter(["O","Q","R","S"]))
