import pandas as pd

# Read the CSV file
df = pd.read_csv('dataset/OVS.csv')

# Get the unique categories in the label column
categories = df['Label'].unique()

# Initialize an empty dataframe to store the selected data
selected_data = pd.DataFrame()

r = 110978

# Calculate the number of rows to select from each category
rows_per_category = r // len(categories)

# Iterate over each category
for category in categories:

    # Get the rows for the current category
    category_df = df[df['Label'] == category]

    print(category)

    # Select the required number of rows (if available) and 85 columns
    selected_rows = category_df.sample(min(rows_per_category, len(category_df))).iloc[:, :85]

    # Append the selected rows to the selected data
    selected_data = pd.concat([selected_data, selected_rows])

# If the total number of rows is less than 110978, add more rows from the categories with the most rows
while len(selected_data) < r:
    for category in categories:
        category_df = df[df['Label'] == category]
        if len(category_df) > rows_per_category:
            additional_rows = category_df.sample(min(r - len(selected_data), len(category_df) - rows_per_category)).iloc[:, :85]
            selected_data = pd.concat([selected_data, additional_rows])
            if len(selected_data) >= r:
                break

# Append the selected data to train_data.csv
selected_data.to_csv('train_data.csv', mode='a', header=False, index=False)

# Get the remaining rows for the test set
test_data = pd.concat([df, selected_data, selected_data]).drop_duplicates(keep=False)

# Append the test data to test_data.csv
test_data.to_csv('test_data.csv', mode='a', header=False, index=False)