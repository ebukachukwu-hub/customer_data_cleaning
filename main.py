from src.extract import Extract
from src.transform import Transform


extract = Extract()
transform = Transform()

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

extract.stop()