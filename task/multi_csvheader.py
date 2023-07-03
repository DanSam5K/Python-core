from multiprocessing import Pool
from typing import List

def is_valid_header(header: List[str]) -> bool:
    mandatory_columns = ['column1', 'column2', 'column3']  # Example list of mandatory columns

    missing_columns = [column for column in mandatory_columns if column not in header]
    if missing_columns:
        raise Exception(f"Missing mandatory columns: {', '.join(missing_columns)}")

    return True

def process_csv(filename: str):
    # Read the CSV file and extract the header
    with open(filename, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')

    try:
        is_valid_header(header)
        print("Header is valid.")
    except Exception as e:
        print(f"Header validation failed: {str(e)}")

if __name__ == '__main__':
    pool = Pool()
    pool.apply_async(process_csv, ('large_file.csv',))
    pool.close()
    pool.join()