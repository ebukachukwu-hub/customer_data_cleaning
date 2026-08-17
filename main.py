from src.extract import Extract
from src.transform import Transform
from src.load import Load
from src.report import Report

extract = Extract()
transform = Transform()
load = Load()
report = Report()

df = extract.read_csv("data/raw/customers.csv")

print("=== BEFORE CLEANING ===")
df.show()

df = transform.clean_text(df)

print("=== AFTER TEXT CLEANING ===")
df.show()

df = transform.handle_missing_values(df)

print("=== AFTER HANDLING MISSING VALUES ===")
df.show()

df = transform.convert_data_types(df)

print("=== AFTER CONVERTING DATA TYPES ===")
df.show()

df = transform.validate_data(df)

print("=== AFTER DATA VALIDATION ===")
df.show()

df = transform.remove_duplicates(df)

print("=== AFTER REMOVING DUPLICATES ===")
df.show()

df = transform.detect_income_outliers(df)

print("=== AFTER DETECTING INCOME OUTLIERS ===")
df.show()

df = transform.data_quality_check(df)

print("\n=== FINAL CLEAN DATA ===")
df.show()

print("\n" + "=" * 50)
print("CUSTOMER DATA REPORT")
print("=" * 50)

report.total_customers(df)
report.average_age(df)
report.average_income(df)
report.customers_by_city(df)
report.customers_by_gender(df)

print("\n=== SAVING CLEAN DATA ===")

load.save_csv(df,
               "data/clean/customers_clean.csv")
load.save_parquet(df,
                   "data/clean/customers_clean.parquet")

extract.stop()