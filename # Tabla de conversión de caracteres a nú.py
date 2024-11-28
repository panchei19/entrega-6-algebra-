
tabla_conversion = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, 
    '*': 27, ' ': 28
}

tabla_inversa = {v: k for k, v in tabla_conversion.items()}

modulo = 29

def encriptar_criptosistema_1(texto, a, b):
    texto = texto.upper()
    numeros = [tabla_conversion[char] for char in texto if char in tabla_conversion]
    encriptado = [(a * num + b) % modulo for num in numeros]
    return "".join([tabla_inversa[n] for n in encriptado])

def desencriptar_criptosistema_1(texto_enc, a, b):
    texto_enc = texto_enc.upper()
    a_inv = pow(a, -1, modulo)
    numeros_enc = [tabla_conversion[char] for char in texto_enc if char in tabla_conversion]
    desencriptado = [(a_inv * (num - b)) % modulo for num in numeros_enc]
    return "".join([tabla_inversa[n] for n in desencriptado])

def analizar_frecuencia(texto):
    texto = texto.upper()
    
    frecuencia = {}
    for i, char in enumerate(texto):
        if char in tabla_conversion:
            if char not in frecuencia:
                frecuencia[char] = {'count': 1, 'positions': [i]}
            else:
                frecuencia[char]['count'] += 1
                frecuencia[char]['positions'].append(i)
    
    if frecuencia:
        letra_mas_frecuente = max(frecuencia, key=lambda x: frecuencia[x]['count'])
        return {
            'most_frequent_letter': letra_mas_frecuente,
            'frequency': frecuencia[letra_mas_frecuente]['count'],
            'positions': frecuencia[letra_mas_frecuente]['positions']
        }
    return None

def main():
    a = 3  
    b = 1  
    
    texto_original = "EN EL MAPA MIRAGE EL EQUIPO ANTITERRORISTA PLANEA DESACTIVAR LA BOMBA COLOCADA EN EL SITIO A POR LOS TERRORISTAS"

    texto_encriptado = encriptar_criptosistema_1(texto_original, a, b)
    print("Texto Original:", texto_original)
    print("Texto Encriptado:", texto_encriptado)

    texto_desencriptado = desencriptar_criptosistema_1(texto_encriptado, a, b)
    print("Texto Desencriptado:", texto_desencriptado)
    
    print("Verificación de Desencriptación:", texto_desencriptado == texto_original)

    frecuencia_original = analizar_frecuencia(texto_original)
    print("\nAnálisis de Frecuencia (Texto Original):")
    print(f"Letra más frecuente: {frecuencia_original['most_frequent_letter']}")
    print(f"Frecuencia: {frecuencia_original['frequency']}")
    print(f"Posiciones: {frecuencia_original['positions']}")

    frecuencia_encriptado = analizar_frecuencia(texto_encriptado)
    print("\nAnálisis de Frecuencia (Texto Encriptado):")
    print(f"Letra más frecuente: {frecuencia_encriptado['most_frequent_letter']}")
    print(f"Frecuencia: {frecuencia_encriptado['frequency']}")
    print(f"Posiciones: {frecuencia_encriptado['positions']}")

if __name__ == "__main__":
    main()