import getpass

def guess_word(secret_word, test_letter, attempt_word):
    """
    Checkea si la letra está en secret word y si la palabra es igual
    ARG: secret_word = Palabra Secreta
    test_letter = Letra a verificar que se encuentra en Secret Word
    attempt_word = Palabra que debe ser igual que Secret Word
    ---
    Return:
    Print: La letra "X" está en la palabra Secret Word
    Print: La palabra "XXXX" es igual que Secret Word 
    """
    # Aqui va la logica
    letter_in_word = test_letter in secret_word
    if (letter_in_word == True):
        letter_in_word = " está en la palabra "
    else:
        letter_in_word = " no está en la palabra "

    print("La letra ", test_letter, letter_in_word, secret_word)

    #Logica
    result_word = attempt_word == secret_word
    if (result_word == True):
        result_word = " es igual que "
    else:
        result_word = " no es igual que "
    print("La palabra ", attempt_word, result_word, secret_word)


def main():
    print("=== Letter and Word Guessing Game ===")
    secret_word = getpass.getpass("Introduce Palabra Secreta: ")
    test_letter = input("Introduce letra: ")
    attempt_word = input("Introduce palabra: ")
    guess_word(secret_word, test_letter, attempt_word)

if __name__ == "__main__":
    main()