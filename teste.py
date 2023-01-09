from datetime import datetime

born = 1996
now = datetime.now()
age = now.year - born

def henrico() -> dict:
    return {
      "nome": "Henrico Nardelli Bela",
      "idade": age,
      "hobbies": ["Programacao", "Cinema", 
                  "Series", "Games"]
    }
    
nome, idade, hobbies = henrico().values()
print(f"Nome: {nome}\nIdade: {idade}\nHobbies: {hobbies}")