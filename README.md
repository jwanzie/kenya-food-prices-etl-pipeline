### Kenya Food Prices Dataset: Data Exploration

### Overview

This document highlights the key data quality issues identified during the cleaning and exploratory phase of the Kenya food prices dataset(`wfp_food_prices_ken.csv`) along with how they were resolved.

### Data Issues Observed

#### 1. Missing Values

47 records associated with a single market(Hola (Tana River)) had missing values in admin1, admin2, latitude, longitude. Since all these records shared a similar market, the missing fields were filled in using location data for Tana River County rather than dropping the rows therefore preserving the valid price data.

#### 2. Mixed Units Within a Commodity

Some commodities contain multiple `unit_type` values depending on the market or vendor eg. Kale is sold under both `Bunch` and `KG`. This meant that `unit_type` couldn't be treated as a fixed attribute for dimension-table purposes. Retaining it at the staging level instead of in dim_commodity preserved accuracy without forcing a false one-to-one mapping.

#### 3. Inconsistent Units

Within the `unit` column, there's a mix of plain units(`L`, `Bunch`) and other's containing quantities(`400 KG, 500ML`). This reflected a genuine difference on how commodities are sold adn the column split to two separate fields for `quantity` and `unit_type` to enable accurate calculation of price per unit
