import exponential

def main():
    try:
        numero = int(input("Inserisci un numero intero: "))
        funzione_esponenziale = exponential.FunzioneEsponenziale(numero)
        risultato = funzione_esponenziale.calcola(2)  # Esempio: calcola la funzione esponenziale con base 2
        print("Il risultato della funzione esponenziale è:", risultato)
    except ValueError:
        print("Errore: Devi inserire un numero intero.")

if __name__ == "__main__":
    main()
