def createHTML(listy):
    createdFile = open("converted.html","w+")
    #check for no no characters and replace them with regex
    
    #beginings
    createdFile.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n<title>'+listy[0]+'</title>\n<link href="http://fonts.googleapis.com/css?family=Corben:bold" rel="stylesheet" type="text/css">\n</head>\n<style type="text/css">\nh1{\nfont-family: "Corben", Georgia, Times, serif;\nfont-size: 300%;}\np{\nfont-family: courier;\nword-wrap: break-word;\nfont-size: 160%;}\nbody {background-color: powderblue;}\n</style>\n<body>\n<center>\n<u><h1>'+listy[0]+'</h1></u>\n</center><br>\n<p>\n')
    #data
    #basic text/ or info<hr>
    listy.pop(0)
    for line in listy:
        createdFile.write(line+"<br>")
    #endings
    createdFile.write('\n</p>\n</body>\n</html>')
    createdFile.close()

try:
    file = open('words.txt', 'r')#r is for reading
    content = file.readlines()
    content = [x.rstrip('\n') for x in content]
    file.close()
    createHTML(content)
except:
    print("couldn't find file dumbo")
#TODO:make regex that finds characters that fucks with the thing such as \n or any tag make it only input data.
#TODO:make regex that finds if there is a link with a picture or website

