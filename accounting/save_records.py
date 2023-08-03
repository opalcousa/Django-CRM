import csv
import os
from .accounting_record import AccountingRecord

def save_records(records: list[AccountingRecord], filename: str, fieldnames: list[str]):
    """Save the generated records in a .csv file in the 'reports' subdirectory."""

    if not os.path.exists('reports'):
        os.makedirs('reports')

    with open(f'reports/{filename}', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for record in records:
            writer.writerow(record)
