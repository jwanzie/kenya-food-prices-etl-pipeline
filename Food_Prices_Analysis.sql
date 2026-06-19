CREATE DATABASE food_prices_ken;

USE food_prices_ken;

CREATE TABLE raw_food_prices (
date DATETIME,
admin1 VARCHAR(100),
admin2 VARCHAR(100),
market VARCHAR(100),
market_id INT,
latitude NUMERIC(9, 6),
longitude NUMERIC(9, 6),
category VARCHAR(100),
commodity VARCHAR(150),
commodity_id INT,
unit VARCHAR(50),
priceflag VARCHAR(150),
pricetype VARCHAR(150),
currency CHAR(3),
price NUMERIC(14, 4),
usdprice NUMERIC(14, 4));

DESCRIBE raw_food_prices;

SELECT COUNT(*) FROM raw_food_prices;

SELECT * FROM raw_food_prices LIMIT 5;

#latest price in the Nairobi market
SELECT date, market, commodity, unit, price, currency
FROM raw_food_prices
WHERE admin1 = 'Nairobi'
ORDER BY date DESC
LIMIT 20;

#Aggregates; avg, min and max price per commodity
SELECT commodity, 
	ROUND(AVG(price), 2) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    COUNT(*) AS total_records
FROM raw_food_prices
GROUP BY commodity
ORDER BY avg_price DESC;

#Commodities with >10 markets
SELECT commodity, COUNT(DISTINCT market) AS market_count -- REVIEW WITHOUT DISTINCT
FROM raw_food_prices
GROUP BY commodity
HAVING market_count > 10
ORDER BY market_count DESC;

#avg price by county/year
SELECT admin2, EXTRACT(YEAR FROM date) AS year, ROUND(AVG(price), 2) as avg_price
FROM raw_food_prices
GROUP BY admin2, year
ORDER BY admin2, year;

#filter recent data
SELECT date, admin2, market, commodity, price
FROM raw_food_prices
WHERE date >= '2025-01-01'
ORDER BY date DESC;

#wholesale vs retail avg price per commodity
SELECT commodity, pricetype, ROUND(AVG(price), 2) AS avg_price, COUNT(*) AS records
FROM raw_food_prices
GROUP BY commodity, pricetype
ORDER BY commodity, pricetype;

SELECT * 
FROM raw_food_prices
WHERE market_id = 1854;

SELECT * 
FROM raw_food_prices
WHERE market = 'Hola (Tana River)';

#cleaned data staging table
CREATE TABLE staging_food_prices (
date DATE,
admin1 VARCHAR(100),
admin2 VARCHAR(100),
market VARCHAR(100),
market_id INT,
latitude DECIMAL(9, 2),
longitude DECIMAL(9, 2),
category VARCHAR(150),
commodity VARCHAR(150),
commodity_id INT,
priceflag VARCHAR(100),
pricetype VARCHAR(100),
currency CHAR(3),
price DECIMAL(10, 2),
usdprice DECIMAL(10, 2),
year INT,
month INT,
quantity INT,
unit_type VARCHAR(50),
price_per_unit DECIMAL(10, 2)
);

SELECT * FROM staging_food_prices LIMIT 5;
