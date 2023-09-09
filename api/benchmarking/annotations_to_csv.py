import pandas as pd
import sys
import os

input_file_path = sys.argv[1]
annotations = pd.read_excel(input_file_path, engine="openpyxl")
annotations = annotations[annotations.url1.notna()]
annotations['group_list'] = annotations['grouped'].str.split(',')
doi_df = annotations.explode('group_list')[["group_list", "url1", "url2", "url3"]]
doi_df[doi_df.columns] = doi_df.apply(lambda x: x.str.strip())
output_file_name = os.path.basename(input_file_path).split('.')[0] + "_annotations.csv"
doi_df.to_csv(output_file_name, index=False, encoding='utf-8')