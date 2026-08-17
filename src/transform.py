from pyspark.sql.functions import col, trim, upper, initcap, sum


class Transform:

    def clean_text(self, df):

        df = df.withColumn(
            "Name",
            trim(col("Name"))
        )

        df = df.withColumn(
            "Gender",
            upper(trim(col("Gender")))
        )

        df = df.withColumn(
            "City",
            initcap(trim(col("City")))
        )

        return df

    def check_nulls(self, df):

        null_counts = df.select([
            sum(
                col(c).isNull().cast("int")
            ).alias(c)
            for c in df.columns
        ])

        null_counts.show()

        return df

    def handle_missing_values(self, df):

        # Remove records where customer name is missing
        df = df.dropna(subset=["Name"])

        return df

    def convert_data_types(self, df):

    # Convert Age from string to integer.
    # Invalid values such as "abc" become NULL.
        df = df.withColumn(
        "Age",
        df["Age"].try_cast("integer")
    )

        return df

    def validate_data(self, df):

    # Remove invalid or missing ages
        df = df.filter(
            (col("Age").isNotNull()) &
            (col("Age") >= 18) &
            (col("Age") <= 100)
        )

    # Income must not be negative
        df = df.filter(
            col("Income") >= 0
        )

        return df

    def remove_duplicates(self, df):
        # Remove duplicate records based on all columns

        df = df.dropDuplicates()

        return df

    def detect_income_outliers(self, df):

        # Get the 25th and 75th percentiles
        quantiles = df.approxQuantile(
            "Income",
            [0.25, 0.75],
            0.0
        )

        q1 = quantiles[0]
        q3 = quantiles[1]

        # Calculate the Interquartile Range
        iqr = q3 - q1

        # Calculate the boundaries
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)

        print("\n=== INCOME OUTLIER DETECTION ===")
        print(f"Q1: {q1}")
        print(f"Q3: {q3}")
        print(f"IQR: {iqr}")
        print(f"Lower Bound: {lower_bound}")
        print(f"Upper Bound: {upper_bound}")

        # Show potential outliers
        outliers = df.filter(
            (col("Income") < lower_bound) |
            (col("Income") > upper_bound)
        )

        print("\nPotential Income Outliers:")
        outliers.show()

        return df