import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('patient_data.csv')
print(f'{data.head(5)}')
rows = len(data)
print(f'number of patients: {rows}')
print(f'mean WBC count: {data['WBC_Count'].mean()}')
print(f'min WBC count: {data['WBC_Count'].min()}')
print(f'max WBC count: {data['WBC_Count'].mean()}')
unique_conditions = data['WBC_Count'].unique()
num_unq_con = len(unique_conditions)
print(f'number of unique WBC count: {num_unq_con}: {unique_conditions}')

# Filter patients with WBC count > 10,000
# TODO: Create a DataFrame 'high_wbc' containing patients with WBC_Count > 10000
high_wbc = data['WBC_Count']>10000
print("\nPatients with WBC count above 10,000:")
print(high_wbc)

# Filter patients with the condition 'Healthy'
# TODO: Create a DataFrame 'healthy_patients' containing patients with Condition == 'Healthy'
healthy_patients = data['Condition'] == 'Healthy'
print("\nPatients with the condition 'Healthy':")
print(healthy_patients)
# Count patients by condition
# TODO: Use a method to count the number of patients in each condition and store in 'condition_counts'
condition_counts = data['Condition'].value_counts()
print("\nNumber of patients by condition:")
print(condition_counts)

plt.figure(figsize=(8, 5))
condition_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Patients by Condition', fontsize=14)
plt.xlabel('Condition', fontsize=12)
plt.ylabel('Number of Patients', fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Scatter plot of Age vs. WBC Count
plt.figure(figsize=(8, 5))
plt.scatter(data['Age'], data['WBC_Count'], color='purple', alpha=0.7)
plt.title('Age vs. WBC Count', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('WBC Count', fontsize=12)
plt.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()