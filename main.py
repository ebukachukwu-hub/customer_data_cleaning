from src.extract import Extract
from src.transform import Transform


extract = Extract()
transform = Transform()

df = extract.read_csv("data/raw/customers.csv")

print("=== BEFORE CLEANING ===")
df.show()

df = transform.clean_text(df)

df = transform.handle_missing_values(df)

print("=== AFTER TEXT CLEANING ===")
df.show()

print("=== NULL VALUES ===")
transform.check_nulls(df)

extract.stop()