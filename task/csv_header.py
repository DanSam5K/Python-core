from typing import List

def is_valid_header(header: List[str]) -> bool:
    mandatory_col = ['column1', 'column2', 'column3'] # Sample of must have columns
    missing_col = [col for col in mandatory_col if col not in header]
    if missing_col:
        raise Exception(f"Missing mandatory columns:{', '.join(missing_col)}")
    
    return True

header = ['column1', 'column4'] # failed to valid header
header2 = ['column1', 'column2', 'column3', 'column4']  # valid Example CSV header


try:
    is_valid_header(header)
    print("Header is valid.")
except Exception as e:
    print(f"Header validation failed: {str(e)}")