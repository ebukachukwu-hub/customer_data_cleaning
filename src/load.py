class Load:

    def save_csv(self, df, path):

        (
            df.write
            .mode("overwrite")
            .option("header", True)
            .csv(path)
        )

        print("=" * 50)
        print(f"CSV successfully saved to:\n{path}")
        print("=" * 50)

    def save_parquet(self, df, path):

        (
            df.write
            .mode("overwrite")
            .parquet(path)
        )

        print("=" * 50)
        print(f"Parquet successfully saved to:\n{path}")
        print("=" * 50)