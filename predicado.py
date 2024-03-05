verbos = ["correu", "andou"]
frase = ["o", "cachorro", "correu", "ate", "o", "parque", ",", "e", "o", "gato", "andou", "ate", "la"]
final = [len(frase)]
verbo_inicio = []
predicados = -1

for palavra in frase:    

    if palavra in verbos:
        predicados += 1
        verbo_inicio.append(frase.index(palavra))

    if palavra == ",":
        final[predicados] = frase.index(palavra)
    
    if len(final) < len(verbo_inicio):
        final.append(len(frase))

if predicados == -1:
    print("Essa frase não possui predicados")
else:
    print(f"Essa frase possui {predicados + 1} predicados:")
    for i in range(predicados + 1):
        print(frase[verbo_inicio[i]:final[i]])
