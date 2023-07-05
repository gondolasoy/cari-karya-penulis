def find_born_year(x):
    words = ""
    if ("born") in x:
        num_char = x.index("born")
        for i in range(num_char, num_char + 15):
            words += f"{x[i]} " 
    else:
        for i in range(0, 100):
            words += f"{x[i]} " 

    words = words.replace(",", "").replace(".", "").replace(")", "")
    words = words.split()

    for word in words:
        try:
            word = int(word)
            if len(str(word)) == 4:
                return(word)
        except:
            return(find_born_year_alternative(x))

def find_born_year_alternative(x):
    words = ""
    for i in range(0, 100):
        words += f"{x[i]} " 

    words = words.replace(",", "").replace(".", "").replace(")", "")
    words = words.split()

    for word in words:
        try:
            word = int(word)
            if len(str(word)) == 4:
                return(word)
        except:
            pass  