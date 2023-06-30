import asyncio
from typing import List

async def is_valid_header(header: List[str]) -> bool:
    mandatory_columns = ['column1', 'column2', 'column3']  # Example list of mandatory columns

    missing_columns = [column for column in mandatory_columns if column not in header]
    if missing_columns:
        raise Exception(f"Missing mandatory columns: {', '.join(missing_columns)}")

    return True

async def process_csv(filename: str):
    # Read the CSV file and extract the header
    with open(filename, 'r') as file:
        lines = await file.readlines()
        header = lines[0].strip().split(',')

    try:
        await is_valid_header(header)
        print("Header is valid.")
    except Exception as e:
        print(f"Header validation failed: {str(e)}")

asyncio.run(process_csv('large_file.csv'))