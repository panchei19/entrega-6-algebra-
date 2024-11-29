import numpy as np
from sympy import Matrix
from collections import Counter

tabla_conversion = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, 
    '*': 27, ' ': 28
}
tabla_inversa = {v: k for k, v in tabla_conversion.items()}
modulo = 29

def dividir_en_bloques(texto, tamano_bloque=3):
    texto = ''.join(char for char in texto.upper() if char in tabla_conversion)
    
    while len(texto) % tamano_bloque != 0:
        texto += " "
    
    return [texto[i:i+tamano_bloque] for i in range(0, len(texto), tamano_bloque)]

def bloques_a_vectores(bloques):
    return [np.array([[tabla_conversion[char]] for char in bloque]) for bloque in bloques]

def encriptar_criptosistema_vectorial(texto, T, b):
    bloques = dividir_en_bloques(texto)
    vectores = bloques_a_vectores(bloques)
    
    encriptados = []
    for vector in vectores:
        vec_encriptado = (T @ vector + b) % modulo
        encriptados.append(vec_encriptado)

    texto_encriptado = "".join(
        "".join(tabla_inversa[int(val[0])] for val in vec) 
        for vec in encriptados
    )
    
    return texto_encriptado, encriptados

def desencriptar_criptosistema_vectorial(vectores_encriptados, T, b):
    T_inv_matrix = Matrix(T).inv_mod(modulo)
    T_inv = np.array(T_inv_matrix.tolist(), dtype=int)
    
    desencriptados = []
    for vector in vectores_encriptados:
        vector_arr = np.array(vector, dtype=int)
        vec_desencriptado = (T_inv @ (vector_arr - b)) % modulo
        desencriptados.append(vec_desencriptado)
    
    texto_desencriptado = "".join(
        "".join(tabla_inversa[int(val[0])] for val in vec) 
        for vec in desencriptados
    )
    
    return texto_desencriptado

def analizar_frecuencias(texto):
    texto_filtrado = ''.join(char for char in texto.upper() if char in tabla_conversion)
    frecuencias = Counter(texto_filtrado)
    
    if frecuencias:
        letra_mas_comun = frecuencias.most_common(1)[0][0]
        posiciones = [i for i, char in enumerate(texto_filtrado) if char == letra_mas_comun]
        
        return {
            'letra': letra_mas_comun,
            'frecuencia': frecuencias[letra_mas_comun],
            'posiciones': posiciones
        }
    
    return None

def main():
    T = np.array([
        [1, 2, 3],
        [0, 1, 4],
        [1, 0, 1]
    ])
    
    b = np.array([[1], [2], [3]])

    texto_original = (
        "EN EL MAPA MIRAGE EL EQUIPO ANTITERRORISTA PLANEA DESACTIVAR LA BOMBA COLOCADA EN EL SITIO A POR LOS TERRORISTAS"
    )
    
    texto_encriptado, vectores_encriptados = encriptar_criptosistema_vectorial(texto_original, T, b)

    frecuencia_original = analizar_frecuencias(texto_original)
    print("Análisis de frecuencias (Texto Original):")
    print(f"Letra más repetida: '{frecuencia_original['letra']}'")
    print(f"Frecuencia: {frecuencia_original['frecuencia']}")
    print(f"Posiciones: {frecuencia_original['posiciones']}")

    frecuencia_encriptado = analizar_frecuencias(texto_encriptado)
    print("\nAnálisis de frecuencias (Texto Encriptado):")
    print(f"Letra más repetida: '{frecuencia_encriptado['letra']}'")
    print(f"Frecuencia: {frecuencia_encriptado['frecuencia']}")
    print(f"Posiciones: {frecuencia_encriptado['posiciones']}")
    
    texto_desencriptado = desencriptar_criptosistema_vectorial(vectores_encriptados, T, b)
    
    print("\n--- Resultados ---")
    print("Texto Original:      ", texto_original)
    print("Texto Encriptado:    ", texto_encriptado)
    print("Texto Desencriptado: ", texto_desencriptado)
    print("\nVerificación de Desencriptación:", texto_desencriptado == texto_original)
    
    print("\n--- Vulnerabilidad ---")
    print("Este criptosistema comparte vulnerabilidades similares al anterior:")
    print("1. Si un espía conoce la matriz T y el vector b, puede desencriptar el mensaje")
    print("2. La desencriptación requiere conocer la inversa modular de T")
    print("3. La seguridad depende de mantener T y b secretos")

if __name__ == "__main__":
    main()