import argparse
import csv
from datetime import datetime
from Bio import Entrez

# Configure Entrez email
Entrez.email = "guy.haim@weizmann.ac.il"

def search_ncbi(database, term, number):
    """Search the NCBI database for a term and return IDs and total count."""
    handle = Entrez.esearch(db=database, term=term, retmax=number)
    record = Entrez.read(handle)
    handle.close()
    ids = record['IdList']
    total_count = record['Count']
    return ids, total_count

def fetch_data(database, ids):
    """Fetch records by IDs from the NCBI database."""
    handle = Entrez.efetch(db=database, id=ids, rettype="gb", retmode="text")
    return handle.read()

def save_to_files(records, term):
    """Save records to individual files and return file names."""
    filenames = []
    for i, record in enumerate(records, start=1):
        filename = f"{term}_record_{i}.txt"
        with open(filename, "w") as file:
            file.write(record)
        filenames.append(filename)
    return filenames

def append_to_csv(log_file, date, database, term, number, total_count):
    """Append search metadata to a CSV file."""
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, database, term, number, total_count])

def main():
    # Step 1: Parse command-line arguments
    parser = argparse.ArgumentParser(description="Download data from NCBI.")
    parser.add_argument("--database", type=str, default="nucleotide", help="NCBI database (default: nucleotide).")
    parser.add_argument("--term", type=str, required=True, help="Search term.")
    parser.add_argument("--number", type=int, default=10, help="Number of items to fetch (default: 10).")
    args = parser.parse_args()

    database = args.database
    term = args.term
    number = args.number

    # Step 2: Search NCBI database
    print(f"Searching for '{term}' in the '{database}' database...")
    ids, total_count = search_ncbi(database, term, number)

    # Step 3: Fetch records
    print(f"Fetching up to {len(ids)} records...")
    records = [fetch_data(database, [id]) for id in ids]

    # Step 4: Save records to files
    print(f"Saving records to files...")
    filenames = save_to_files(records, term)
    for filename in filenames:
        print(f"Saved: {filename}")

    # Step 5: Log metadata to CSV
    log_file = "ncbi_search_log.csv"
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    append_to_csv(log_file, current_date, database, term, number, total_count)
    print(f"Metadata saved to {log_file}.")

if __name__ == "__main__":
    main()
