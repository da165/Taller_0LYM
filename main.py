file= open("test1.txt", "r")
lista_aux=file.readlines()
unidos=",".join(lista_aux)
tokens1=unidos.split(":")
print(len(tokens1))
tokens=[]
pos=0
while pos< len(tokens1):
    tokens.append(tokens1[pos])
    tokens.append(":")
    pos+=1
print(tokens)

#Este codigo sirve para separar la cadena que nos mandan por input y lo separa en tokens, toknes es una lista que te isrve para comparar
#cada elemento de la lista tokens la debes comparar con las variables que dio la profe en el taller
#las variables deben existir en el lenguaje si no devuelve false
R="turn to right"
M="to move forward"
R="to turn right"
C="to drop a chip"
B="to place a balloon"
c="to pickup a chip"
b="to grab a balloon"
P="to pop a balloon"


def parser(tokens):
    variables_declaradas = set()
    procedimientos_declarados = set() 
    i = 0

    while i < len(tokens):
        token = tokens[i]

        
        if token == "|":
            i += 1
            while i < len(tokens) and tokens[i] != "|":
                variables_declaradas.add(tokens[i])
                i += 1
            if i >= len(tokens) or tokens[i] != "|":
                return "False"
            i += 1
            continue

        
        elif token == "proc":
            i += 1
            if i < len(tokens) and ":" in tokens[i]: 
                procedimientos_declarados.add(tokens[i])
                i += 1
                if i < len(tokens) and tokens[i] == "[": 
                    i += 1
                    continue
                else:
                    return "False"

        
        elif token in variables_declaradas and i+2 < len(tokens) and tokens[i+1] == ":=":
            i += 3 
            if tokens[i-1] != ".":
                return "False" 
            continue

        
        elif token in ["put", "move", "turn", "face", "pick"]:
            i += 1 
            if i < len(tokens) and tokens[i] == ":":
                i += 2 
                continue
            else:
                return "False"  

        else:
            return "False" 

    return "True" 