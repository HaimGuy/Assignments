# Given values
C1_values = [8,3,5,1,7,4,10,6,2,5,3,6,8,9] # TODO : at least 10 values
V1 = 2 # TODO:Initial volume
V2 = 6 # TODO: Final volume
C2_values = []
for C1 in C1_values:
    C2 = (C1*V1)/V2
    C2_values.append(C2)
    print(f"Initial concentration: {C1} mg/mL -> Final concentration: {C2:.2f} mg/mL")
# Create an empty list to store slope values
slopes = []

# Calculate the slope for each consecutive pair of points
for i in range(1, len(C1_values)):
    x1, x2 = C1_values[i - 1], C1_values[i]
    y1, y2 = C2_values[i - 1], C2_values[i]
    slope = (y2-y1)/(x2-x1)   # TODO: Calculate the slope using the formula (y2 - y1) / (x2 - x1)

    slopes.append(slope)

# Print the list of calculated slopes
print("Calculated slopes:", slopes)