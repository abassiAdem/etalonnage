def get_calibration_value(line):
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char  # Premier chiffre trouvé
            last_digit = char  # Dernier chiffre trouvé sera toujours mis à jour

    # Si aucun chiffre n'est trouvé, retourner 0
    if first_digit is None or last_digit is None:
        return 0

    # Former le nombre à partir du premier et du dernier chiffre
    return int(first_digit + last_digit)

def solve_calibration_sum(data):
    total = 0
    for line in data.splitlines():
        total += get_calibration_value(line)
    return total

# Lire et traiter les données
with open('document.txt', 'r') as file:
    data = file.read()
    result = solve_calibration_sum(data)
    print(f"La somme de toutes les valeurs de calibration est : {result}")
