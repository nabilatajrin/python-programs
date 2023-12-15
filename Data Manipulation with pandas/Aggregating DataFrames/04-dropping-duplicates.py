# Drop duplicate store/type combinations
store_types = sales[['store','type']]
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales[['store','department']]
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates)
