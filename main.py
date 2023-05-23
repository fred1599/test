import json
from typing import Any, Dict
from typer import Typer, Argument

app = Typer()

MSG_MULTIPLE_DE_5 = "Multiple de 5"
MSG_RIEN_A_AFFICHER = 'Rien à afficher'
CHARACTER_SUBSTITUTION = "$"
SUBSTITUTION_CHARACTER = "_"

def process_line(line: str, line_number: int) -> str:
    """
    Traite une ligne donnée en fonction de divers critères.
    """

    if line_number % 5 == 0:
        return MSG_MULTIPLE_DE_5
    elif CHARACTER_SUBSTITUTION in line:
        return line.replace(' ', SUBSTITUTION_CHARACTER).strip()
    elif line.rstrip().endswith('.'):
        return line.rstrip()
    elif line.startswith('{'):
        return process_json_line(line, line_number)
    else:
        return MSG_RIEN_A_AFFICHER


def process_json_line(line: str, line_number: int) -> str:
    """
    Traite une ligne JSON en ajoutant un champ supplémentaire si elle est correctement formatée.
    """

    try:
        data_dict: Dict[str, Any] = json.loads(line)
        data_dict['pair'] = line_number % 2 == 0
        return json.dumps(data_dict)
    except json.JSONDecodeError:
        return MSG_RIEN_A_AFFICHER


@app.command()
def process_file(file_path: str = Argument(..., help="Le chemin du fichier à traiter")) -> None:
    """
    Ouvre un fichier et traite chaque ligne en utilisant la fonction process_line.
    """

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file):
            new_data: str = process_line(line, line_number)
            print(f"{line_number} : {new_data}")


if __name__ == "__main__":
    app()
