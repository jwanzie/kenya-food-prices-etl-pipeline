import pandas as pd

def clean_data(df):
  # Fill in missing values for Hola (Tana River) market
  df.loc[df['market'] == 'Hola (Tana River)', 'admin1'] = 'Tana River'
  df.loc[df['market'] == 'Hola (Tana River)', 'admin2'] = 'Tana River'
  df.loc[df['market'] == 'Hola (Tana River)', 'latitude'] = -1.0
  df.loc[df['market'] == 'Hola (Tana River)', 'longitude'] = 40.0

  # Parse dates and derive year and month
  df['date'] = pd.to_datetime(df['date'])

  df['year'] = df['date'].dt.year
  df['month'] = df['date'].dt.month

  # Standardize unit column by adding '1' prefix to units without a quantity
  df['unit'] = df['unit'].apply(lambda x: '1 ' + x if ' ' not in x else x)
  
  # Split unit into quantity and unit_type 
  df['quantity'] = df['unit'].apply(lambda x: float(x.split(' ')[0]) if ' ' in x else 1)
  df['unit_type'] = df['unit'].apply(lambda x: x.split(' ')[1] if ' ' in x else x)

  # Calculate price per unit 
  df['price_per_unit'] = df['price'] / df['quantity']
  df['price_per_unit'] = df['price_per_unit'].round(2)

  # Drop original unit column
  df.drop(columns = ['unit'], inplace = True)

  # Convert quantity to integer
  df['quantity'] = df['quantity'].astype(int)

  return df

