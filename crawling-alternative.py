import wikipedia as wiki
import webbrowser
import caribornyear
from caribornyear import find_born_year

def find_paragraph_wrote(x):
    words_final = []
    num_char = []
    wordingan = ""
    
    search_word = "wrote"

    for index, word in enumerate(x):
        if word == search_word:
            num_char.append(index)    

    for list in num_char:
        words = ""
        number = list
        number2 = list - 1

        while "." not in x[number] :
            words += x[number] + ' '
            number += 1
        words += x[number] + ' '

        while "." not in x[number2]:
            words = x[number2] + " " + words
            number2 = number2 - 1
        
        words_final.append(words)
        
    for things in enumerate(words_final):
        wordingan = wordingan + (str(things)[5:-3]) + "\n" + "\n"

    return(wordingan)

figure = input("who is the writer you wanna know about ... ")
content = wiki.page(str(figure)).content
year_born = find_born_year(content.split())
writing = find_paragraph_wrote(content.split())

#print(content)

result = f"{figure} was born in {year_born}\n\nseveral things to know about {figure}'s writing...\n\n{writing}"

# Save the result to a temporary text file
filename = "result.txt"
with open(filename, "w") as file:
    file.write(result)

# Open the text file in the default text editor
webbrowser.open(filename)
 


