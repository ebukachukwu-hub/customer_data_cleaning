from src.extract import Extract


# Create the Extract object
extract = Extract()

# Read the raw customer data
df = extract.read_csv("data/raw/customers.csv")

# Display basic information
print("Rows:", df.count())

print("\nSchema:")
df.printSchema()

print("\nRaw Customer Data:")
df.show()

# Stop Spark
extract.stop()