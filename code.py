string = input() #input string
stringtwo = "" # create the reverse string
for i in reversed(range(len(string))): # loop over the input backwards 
    stringtwo += string[i] # store every letter in the reversed string


if string == stringtwo: # check if they are equal 
    print("YES")
else:
    print("NO")        
    #fin
