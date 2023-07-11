import ast
import pandas as pd


def cleaning_incidents(filename):
    # Import file
    df = pd.read_excel(filename)
    # Feature selection
    df = df[['number', 'caller', 'callerBranch', 'priority', 'operator', 'operatorGroup', 'processingStatus', 'closed']]
    # Iterate over columns and convert string to objects
    for column in df.columns:
        # Find the first non-null element in the column
        first_non_null = df[column].dropna().iloc[0]
        # Find stringified objects
        if isinstance(first_non_null, str) and first_non_null.strip().startswith("{"):
            # Apply ast.literal_eval to convert stringified dictionaries back to actual dictionaries
            df.loc[pd.notna(df[column]), column] = df.loc[pd.notna(df[column]), column].apply(ast.literal_eval)
    object_lists = ["operator", "operatorGroup", "priority", "callerBranch", "processingStatus"]
    # Clean column list on "name"
    for columnName in object_lists:
        df[columnName] = df[columnName].apply(lambda x: x['name'] if isinstance(x, dict) and 'name' in x else None)
    # Clean caller on "dynamicName"
        df["caller"] = df["caller"].apply(lambda x: x['name'] if isinstance(x, dict) and 'name' in x else None)
    # Save file back with recognizable name without overwrite
    df.to_excel(filename.split(".")[0]+"_clean.xlsx", index=False)


cleaning_incidents("Incidents.xlsx")

