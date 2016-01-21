import numpy as np
import pandas as pd

records = pd.read_csv('~/hw0/iowa-liquor-sample.csv')
records = records.astype(str)

mask = np.column_stack(records[col].str.contains('single malt scotch', na=False, case=False) for col in records)
print records.loc[mask.any(axis=1)].shape[0]