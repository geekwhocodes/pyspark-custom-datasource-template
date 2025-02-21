from pyspark.sql import SparkSession

spark: SparkSession = SparkSession.builder \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()
