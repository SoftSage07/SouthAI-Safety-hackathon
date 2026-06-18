# This file merges the advbench_200_unsafe.csv and safe_200.csv into one dataframe and saves it as a csv

import pandas as pd

unsafe_df = pd.read_csv(r"C:\Users\SATI0004\Documents\SouthAI-Safety-hackathon\advbench_200_unsafe.csv")
safe_df = pd.read_csv(r"C:\Users\SATI0004\Documents\SouthAI-Safety-hackathon\safe_200.csv")

print(f"Columns of Unsafe df: {unsafe_df.columns}")
print(f"Columns of Safe df: {safe_df.columns}")

unsafe_cols = unsafe_df[['id', 'prompt', 'label']]
safe_cols = safe_df[['id', 'prompt', 'label']]

mixed_df = pd.concat([unsafe_cols, safe_cols], axis=0, ignore_index=True)

mixed_df["id"] = [f"mixed_{i:05d}" for i in range(1, len(mixed_df) + 1)]

mixed_df.to_csv("final_modified_advbench.csv", index=False)




