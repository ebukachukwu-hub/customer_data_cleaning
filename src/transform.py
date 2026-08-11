from pyspark.sql.functions import col, trim, lower, upper, initcap


class Transform:

    def clean_text(self, df):

        # Remove spaces from the beginning and end of text
        df = df.withColumn(
            "Name",
            trim(col("Name"))
        )

        # Standardize gender
        df = df.withColumn(
            "Gender",
            upper(trim(col("Gender")))
        )

        # Standardize city
        df = df.withColumn(
            "City",
            initcap(trim(col("City")))
        )

        return df