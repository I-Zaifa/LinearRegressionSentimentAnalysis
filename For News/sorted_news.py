import pandas as pd
import glob
import os

data_files = 'financial_news*.csv'
output_file = 'extracted_'
casual_list = []

# print(data_files.iloc[0,2])
# print(data_files.iloc[0,4])

# Sorts the data by extracting only the summaries in full. (The date is formatted later.)
for file in glob.glob(data_files):
    print(file)
    data_file = pd.read_csv(file)

    output_file_name = output_file + file

    print(output_file_name)

    all_the_rows = []

    with open(output_file_name, 'w+', encoding='utf-8', newline='') as output_file:
        for n in range(len(data_file)):
            casual_list = [data_file.iloc[n, 4].replace('\n', '')]
            all_the_rows.append(casual_list)
            print(all_the_rows)
            # df_casual_list.to_csv(output_file, header=False, index=False)

    df_allrows = pd.DataFrame(all_the_rows, columns=['Summary'])
    df_allrows.to_csv(output_file_name, mode='a', index=False)

    output_file = 'extracted_'
    output_file_name = ''
