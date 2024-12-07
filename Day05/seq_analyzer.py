import sys 
filename = sys.argv[1] 

try: 
    with open(filename, "r") as fh: #fh is file holder - to have a position in the file 
    #"r" read (open for reading), "w" write.
        sequence = fh.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(1)
except PermissionError:
    print(f"Error: Insufficient permissions to read '{filename}'.")
    sys.exit(1)

count = [0,0,0,0] # a counter list for nucleutides location - a=0,c=1,t=2,g=3
for char in sequence:
    if char.lower() == 'a':
        count[0] += 1
        continue
    if char.lower() == 'c':
        count[1] += 1 
        continue
    if char.lower() == 't':
        count[2] += 1 
        continue
    if char.lower() == 'g':
        count[3] += 1 
        continue
total = sum(count) #how many nucleotides do I have
if total == 0:
    print("Error: The sequence contains no valid nucleotides (A, C, T, G).")
    sys.exit(1)
prec = [(counter / total) * 100 for counter in count] # calculate percentage

print(f'a = {count[0]} ({prec[0]:.2f}%), c = {count[1]} ({prec[1]:.2f}%), '
      f't = {count[2]} ({prec[2]:.2f}%), g = {count[3]} ({prec[3]:.2f}%)')
       