from pyspark.sql.functions import count, avg


class Report:

    def total_customers(self, df):

        total = df.count()

        print(f"\nTotal Valid Customers: {total}")


    def average_age(self, df):

        average = (
            df.select(
                avg("Age").alias("Average Age")
            )
            .collect()[0][0]
        )

        print(f"Average Customer Age: {round(average, 2)}")


    def average_income(self, df):

        average = (
            df.select(
                avg("Income").alias("Average Income")
            )
            .collect()[0][0]
        )

        print(f"Average Customer Income: {round(average, 2)}")


    def customers_by_city(self, df):

        print("\n=== CUSTOMERS BY CITY ===")

        (
            df.groupBy("City")
            .agg(
                count("*").alias("Customer Count")
            )
            .orderBy("Customer Count", ascending=False)
            .show()
        )


    def customers_by_gender(self, df):

        print("\n=== CUSTOMERS BY GENDER ===")

        (
            df.groupBy("Gender")
            .agg(
                count("*").alias("Customer Count")
            )
            .orderBy("Customer Count", ascending=False)
            .show()
        )