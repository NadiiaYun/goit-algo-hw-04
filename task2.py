import re
from pathlib import Path

def get_cats_info(path):
    relative_path = Path(path)
    absolute_path = relative_path.absolute()

    try: 
        with open(absolute_path, 'r', encoding='utf-8') as fh:
            # Виконання операцій з файлом
            lines = [el.strip() for el in fh.readlines()]
    
        pattern = r"[,]+"
        cats = [re.split(pattern,el) for el in lines]        

        cats_info = []

        for el in cats:
            cats_info.append({"id": el[0], "name": el[1], "age": el[2]}) 

    except Exception as e:
        print(f'Error: {e} with file {absolute_path}')

    return cats_info

cats_info = get_cats_info("./cats.txt")
print(cats_info)