# Website:
https://vinaudit-project-production.up.railway.app/

<img width="661" alt="image" src="https://github.com/user-attachments/assets/8427c070-8d8f-4e3b-945b-7e50d4b2a9e5">

# Database Design and the algorithm to convert text file input to DB:

https://docs.google.com/document/d/1gIDiar6m0R-dlnOq34dhXx4axaCOrgLEogcZVzG6Rk0/edit?usp=sharing

# Analysis

1. Price difference between new cars (x=0) and old cars (x=1)

<img width="469" alt="image" src="https://github.com/user-attachments/assets/b1e734b8-c7d6-4f66-9168-0cd7e146c583">


# How to estimate the price
1. Old Algorithm: Take average of price for a given make, model, year
2. Improvement: Take average of new car's price, used but certified car's price and uncertified car's price. Then take final average of these three prices.
3. If mileage is provided, assume a linear relationship between price and mileage. Use linear regression to predict the price.


# Sample test cases comparing output of raw SQL query and the displayed result on the website

https://docs.google.com/spreadsheets/d/1RIkd_sn0_XnIJXYP4HhbM5jCvP7wEQChvFHkMVd4GDU/edit?usp=sharing
