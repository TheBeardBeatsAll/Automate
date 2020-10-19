#! python3
import os
import openpyxl

def toTextFiles(filename):
    """writes column data in worksheet into text files
    Args:
        filename (str): name of worksheet to read from
    Returns:
        None
    """
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    count = 1

    for colObj in sheet.columns:
        
        with open('chpt13/txtFiles/text-'+str(count)+'.txt', 'w') as file:
            for cellObj in colObj:
                file.write(cellObj.value)

        count += 1


if __name__ == "__main__":
    toTextFiles('chpt13/excelFiles/text-to-cols.xlsx')