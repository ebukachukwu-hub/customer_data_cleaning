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