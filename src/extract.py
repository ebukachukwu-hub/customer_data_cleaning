from pyspark.sql import SparkSession


class Extract:

    def __init__(self):
        self.spark = (
            SparkSession.builder
            .appName("Customer Data Cleaning")
            .getOrCreate()
        )

    def read_csv(self, path):

        df = (
            self.spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(path)
        )

        return df

    def stop(self):
        self.spark.stop()