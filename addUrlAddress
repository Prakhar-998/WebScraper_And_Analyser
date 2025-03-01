import pandas as pd

input_file = "input.xlsx"
output_file = "output.xlsx"

input_df = pd.read_excel(input_file)
output_df = pd.read_excel(output_file)

if "URL" in input_df.columns and "URL" in output_df.columns:
    output_df["URL"] = input_df["URL"]

    output_df.to_excel(output_file, index=False)
    print("URL column replaced successfully!")
else:
    print("Required columns not found in the files.")

