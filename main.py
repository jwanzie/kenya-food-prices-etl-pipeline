from extract import load_data
from clean import clean_data
from quality_checks import run_all_checks
from load import load_to_mysql

csv_path = '/Users/lilianmaina/Desktop/Projects/DataEngineeringProject/wfp_food_prices_ken.csv'

def main():
  """ 
  Runs the full ETL pipeline
  1. Extract: load raw CSV
  2. Clean: apply all cleaning transformation
  3. Quality Checks: validate cleaned data
  4. Load: push to MySQL
  """
  
  df = load_data(csv_path)
  print(f'Loaded {len(df)} rows.')

  df = clean_data(df)

  passed = run_all_checks(df)
  if not passed:
    print('Quality checks failed. Stopping pipeline')
    return 

  load_to_mysql(df)

if __name__ == '__main__':
  main()