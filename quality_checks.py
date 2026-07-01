import pandas as pd

def check_missing_values(df, critical_columns):
  missing = df[critical_columns].isnull().sum()
  if missing.sum() > 0:
    print('Missing values found.', missing[missing > 0])
    return False
  print('No missing values')
  return True

def check_negative_prices(df, price_column = 'price'):
  negative_count = (df[price_column] < 0).sum() 
  if negative_count > 0:
    print(f'Found {negative_count} rows with negative prices')
    return False
  print('No negative prices found')
  return True

def check_date_range(df, date_column = 'date', min_year = 2000, max_year = None):
  if max_year is None:
    max_year = pd.Timestamp.now().year

  too_old = (df[date_column].dt.year < min_year).sum()
  too_new = (df[date_column].dt.year > max_year).sum()

  if too_old > 0 or too_new > 0:
    print(f'Found {too_old} rows before {min_year} and {too_new} rows after {max_year}.')
    return False
  print(f'All dates fall within {min_year} and {max_year}.')
  return True

def check_price_per_unit(df, column = 'price_per_unit'):
  invalid_count = df[column].isnull().sum() + (df[column] <= 0).sum()
  if invalid_count > 0:
    print(f'Found {invalid_count} rows with missing or zero {column}.')
    return False
  print(f'All {column} look valid.')
  return True

def run_all_checks(df):
  critical_columns = ['date', 'market', 'commodity', 'price']

  results = [check_missing_values(df, critical_columns),
            check_negative_prices(df),
            check_date_range(df),
            check_price_per_unit(df)]
  
  all_passed = all(results)

  if all_passed:
    print('All quality checks passed.')
  else:
    print('Some quality checks failed. Review output.')

  return all_passed

if __name__ == '__main__':
  # This loads and cleans the data and runs the quality checks

  from extract import load_data
  from clean import clean_data

  csv_path = '/Users/lilianmaina/Desktop/Projects/DataEngineeringProject/wfp_food_prices_ken.csv'

  df = load_data(csv_path)

  df = clean_data(df)

  run_all_checks(df)