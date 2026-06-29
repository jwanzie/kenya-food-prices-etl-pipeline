import pandas as pd

csv_path = '/Users/lilianmaina/Desktop/Projects/DataEngineeringProject/wfp_food_prices_ken.csv'  

def load_data(csv_path):
  df = pd.read_csv(csv_path)
  return df

if __name__ == "__main__":
    df = load_data(csv_path)
    print(df.shape)
    print(df.head())

