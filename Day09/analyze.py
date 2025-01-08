import argparse
import re

def parse_fasta(file_path):
    """Parses a FASTA file and extracts the sequence."""
    with open(file_path, "r") as file:
        content = file.read()
    # Use regex to match lines that do not start with ">" and join them
    sequence = "".join(re.findall(r"^[^>].*", content, re.MULTILINE))
    return sequence.strip()  # Remove trailing newlines or spaces

def find_longest_repeated_subsequence(sequence):
    """Finds the longest repeated subsequence using regular expressions."""
    n = len(sequence)
    longest = ""

    # Try matching substrings of increasing length
    for length in range(1, n // 2 + 1):  # Subsequence cannot be longer than half the sequence
        pattern = f"(.{{{length}}}).*\\1"  # Regex for a substring of 'length' that repeats
        matches = re.findall(pattern, sequence)  # Find all matches of the pattern
        if matches:
            # Find the lexicographically smallest match
            smallest_match = min(matches)
            # Update longest if it's longer or lexicographically smaller
            if len(smallest_match) > len(longest) or (len(smallest_match) == len(longest) and smallest_match < longest):
                longest = smallest_match

    return longest

def analyze_gc_content(sequence):
    """Analyzes the GC content of the sequence using regex."""
    sequence = sequence.upper()  # Ensure case consistency
    # Use regex to count occurrences of G and C
    gc_count = len(re.findall(r"[GC]", sequence))  # Matches 'G' or 'C'
    gc_percentage = (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0
    return gc_percentage

def main():
    parser = argparse.ArgumentParser(description="Analyze sequences from a FASTA or GeneBank file.")
    parser.add_argument("file", help="Path to the FASTA file.")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest repeated subsequence.")
    parser.add_argument("--GC", action="store_true", help="Analyze GC content.")
    
    args = parser.parse_args()
    
    # Parse the sequence from the input file
    sequence = parse_fasta(args.file)
    
    # Perform analyses based on user options
    if args.duplicate:
        longest_dup = find_longest_repeated_subsequence(sequence)
        print(f"Longest repeated subsequence: {longest_dup}")
    
    if args.GC:
        gc_content = analyze_gc_content(sequence)
        print(f"GC content: {gc_content:.2f}%")

if __name__ == "__main__":
    main()
