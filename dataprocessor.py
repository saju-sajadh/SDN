# import csv

# with open('train_data.csv', 'r') as input_file:
#     reader = csv.reader(input_file)
#     with open('output.csv', 'w', newline='') as output_file:
#         writer = csv.writer(output_file)
#         for row in reader:
#             if any(field.strip() for field in row):
#                 writer.writerow(row)

# import pandas as pd

# # Define the path to your CSV file
# csv_file_path = 'test_data.csv'  # Replace with your CSV file path

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# # Remove rows with any null values
# df_cleaned_rows = df.dropna()

# # Remove columns with any null values (if needed)
# df_cleaned = df_cleaned_rows.dropna(axis=1)

# # Save the cleaned DataFrame to a new CSV file
# cleaned_csv_file_path = 'cleaned_file.csv'  # Replace with your desired output file path
# df_cleaned.to_csv(cleaned_csv_file_path, index=False)

# # Check if there are any null values left
# if not df_cleaned.isnull().values.any():
#     print("No null values found in the cleaned DataFrame.")
# else:
#     print("There are still null values in the cleaned DataFrame.")

import pandas as pd

# Load your dataset into a Pandas DataFrame
df = pd.read_csv('test_data.csv')

# Get the unique category labels
category_labels = df['Label'].unique()

# Calculate the number of rows to take from each category
num_rows_per_category = 25000 // len(category_labels)

# Create a new DataFrame to store the sampled data
sampled_df = pd.DataFrame()

# Iterate over each category label
for label in category_labels:
    # Get the rows for this category
    category_df = df[df['Label'] == label]
    
    # If the category has fewer rows than num_rows_per_category, take all rows
    if len(category_df) <= num_rows_per_category:
        sampled_df = pd.concat([sampled_df, category_df])
    else:
        # Otherwise, sample num_rows_per_category rows from this category
        sampled_df = pd.concat([sampled_df, category_df.sample(n=num_rows_per_category)])

# If the sampled data has fewer than 10,000 rows, sample more from the original data
while len(sampled_df) < 25000:
    remaining_rows = 25000 - len(sampled_df)
    sampled_df = pd.concat([sampled_df, df.sample(n=remaining_rows)])

# Reset the index of the sampled DataFrame
sampled_df.reset_index(drop=True, inplace=True)

# Write the sampled data to a new CSV file
sampled_df.to_csv('sampled_data2.csv', index=False)

print("Sampled data written to sampled_data.csv")
