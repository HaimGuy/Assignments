import subprocess
import os

def run_test(test_name, sequence, expected_output):
    # Create a temporary test file
    test_file = "test_seq.txt"
    with open(test_file, "w") as f:
        f.write(sequence)
    
    try:
        result = subprocess.run(
            ["python", "seq_analyzer.py", test_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        
        # Check output
        if result.stdout.strip() == expected_output.strip():
            print(f"{test_name}: PASSED")
        else:
            print(f"{test_name}: FAILED")
            print(f"Expected:\n{expected_output}")
            print(f"Got:\n{result.stdout}")
    
    except Exception as e:
        print(f"{test_name}: ERROR")
        print(e)
    
    # Clean up
    os.remove(test_file)

# Define test cases
tests = [
    {
        "name": "Test 1: Valid Sequence",
        "sequence": "ACGTACGT",
        "expected_output": "a = 2 (25.00%), c = 2 (25.00%), t = 2 (25.00%), g = 2 (25.00%)"
    },
    {
        "name": "Test 2: Empty File",
        "sequence": "",
        "expected_output": "Error: The sequence contains no valid nucleotides (A, C, T, G)."
    },
    {
        "name": "Test 3: Mixed Case Sequence",
        "sequence": "aCgTaCGt",
        "expected_output": "a = 2 (25.00%), c = 2 (25.00%), t = 2 (25.00%), g = 2 (25.00%)"
    },
    {
        "name": "Test 4: Invalid Characters",
        "sequence": "XYZ123",
        "expected_output": "Error: The sequence contains no valid nucleotides (A, C, T, G)."
    },
]

# Run all tests
for test in tests:
    run_test(test["name"], test["sequence"], test["expected_output"])
