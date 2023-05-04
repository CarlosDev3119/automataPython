digitos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
signos = ['"', '=']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

vocabulary = [{'digitos': digitos, 'signos': signos, 'numeros': numeros}]
digitosLetra = vocabulary[0]['digitos'] + vocabulary[0]['numeros']

def runAutomata(input_str):
    state = 0
    variableName = ''
    input_str_len = len(input_str)
    
    for i in range(input_str_len + 1):
        if i < input_str_len:
            char = input_str[i]
        else:
            char = ''
        
        if state == 0:
            if char in vocabulary[0]['digitos']:
                state = 1
                variableName += char
            else:
                return {'resp': False, 'charRecorridos': variableName, 'cadena': input_str}
        
        elif state == 1:
            if char in digitosLetra:
                variableName += char
            elif char == '=':
                variableName += char
                state = 2
            else:
                return {'resp': False, 'charRecorridos': variableName, 'cadena': input_str}
        
        elif state == 2:
            if char == '"':
                variableName += char
                state = 3
            else:
                return {'resp': False, 'charRecorridos': variableName, 'cadena': input_str}
        
        elif state == 3:
            if char in digitosLetra:
                variableName += char
                state = 4
            elif char == '"':
                variableName += char
                state = 5
            else:
                return {'resp': False, 'charRecorridos': variableName, 'cadena': input_str}
        
        elif state == 4:
            if char == '"':
                variableName += char
                state = 5
            else:
                variableName += char
                state = 3
        
        elif state == 5:
            if len(variableName) > 0:
                return {'resp': True, 'charRecorridos': variableName, 'cadena': input_str}
            else:
                return {'resp': False, 'charRecorridos': variableName, 'cadena': input_str}
        
        else:
            return {'resp': False, 'charRecorridos': None, 'cadena': input_str}

    return {'resp': False, 'charRecorridos': None, 'cadena': None}
  
# Ejemplos de uso
print(runAutomata('amo2r="hola"')) 
print(runAutomata('amo2r="hola')) 
print(runAutomata('2amo2r="hola"')) 
    
