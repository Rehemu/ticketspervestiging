import pandas as pd
import ast


def cleaning_incidents(filename):
    df = pd.read_excel(filename)

    # Convert stringified objects to actual dictionaries
    df["results"] = df["results"].apply(ast.literal_eval)

    # Create new columns for the keys of interest
    df["branch_name"] = df.apply(lambda row: row["requester"]["branch"]["name"])

    # Save file back with recognizable name without overwrite
    df.to_excel(filename.split(".")[0] + "_cleaned.xlsx")


# Call the function
cleaning_incidents("changes.xlsx")