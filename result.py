import openpyxl

def read_excel_and_calculate():
    file_path = "tests/test1.xlsx"
    
    try:
        workbook = openpyxl.load_workbook(file_path)
    except Exception as e:
        print(f"Failed to load {file_path}: {e}")
        return 0
    
    sheet = workbook.active
    
    count = 0
    for row in sheet.iter_rows(min_row=2, values_only=True):
        try:
            id, hours, rate, *_ = row  
            print(f"Row data: ID={id}, Hours={hours}, Rate={rate}") # Lai varētu vizualizēt priekš debuggin
            if isinstance(hours, (int, float)) and isinstance(rate, (int, float)):
                salary = hours * rate
                print(f"Calculated Salary: {salary}")
                if salary > 3000:
                    count += 1
        except ValueError as e:
            print(f"Error processing row: {e}")
            continue
    
    workbook.close()
    return count


result = read_excel_and_calculate()
print(f"Result: {result}")