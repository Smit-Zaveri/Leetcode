import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    myvar = pandas.DataFrame(employees)
    return myvar.iloc[:3, :]
    