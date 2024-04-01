import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Merge DataFrame with itself based on managerId
    merged_df = pd.merge(employee, employee, left_on='managerId', right_on='id', suffixes=('_employee', '_manager'))

    # Filter employees who earn more than their managers
    result_df = merged_df[merged_df['salary_employee'] > merged_df['salary_manager']]

    # Select only the 'name_employee' column
    result = result_df[['name_employee']].rename(columns = {'name_employee' : 'Employee'})

    return result
