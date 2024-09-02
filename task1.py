# task1.py
import re
from pathlib import Path

def total_salary(path):  
    relative_path = Path(path)
    absolute_path = relative_path.absolute()

    try: 
        with open(absolute_path, 'r', encoding='utf-8') as fh:
            # Виконання операцій з файлом
            lines = [el.strip() for el in fh.readlines()]
    
        pattern = r"[,]+"
        elements = [re.split(pattern,el) for el in lines]    

        total = 0    

        for el in elements:
            total += float(el[1])

        average = total/len(elements)  

    except Exception as e:
        print(f'Error: {e} with file {absolute_path}')
        total = 0
        average = 0

    return total, average

total, average = total_salary("./salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")