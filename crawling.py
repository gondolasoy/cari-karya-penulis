import wikipedia as wiki

def find_born_year(x):
    words = ""
    if ("born") in x:
        num_char = x.index("born")
        for i in range(num_char, num_char + 15):
            words += f"{x[i]} " 

    words = words.replace(",", "")
    words = words.replace(".", "")
    words = words.split()

    for word in words:
        try:
            word = int(word)
            if len(str(word)) == 4:
                return(word)
        except:
            pass  

def find_paragraph_wrote(x):
    words = ""
    words_final = ""
    num_char = x.index("wrote")
    if ("wrote") in x:
        number = num_char
        number2 = num_char - 1

        while "." not in x[number] :
            words += x[number] + ' '
            number += 1
        words += x[number] + ' '

        while "." not in x[number2]:
            words = x[number2] + " " + words
            number2 = number2 - 1
            
    return(words)

content = wiki.page("Gogol").content
year_born = find_born_year(content.split())
writing = find_paragraph_wrote(content.split())

print(f"{year_born}\n\n{writing}")


 


