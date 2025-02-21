import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    """Create a Spark session for testing."""
    spark = SparkSession.builder \
        .master("local[2]") \
        .appName("pytest-pyspark-datasource-testing") \
        .getOrCreate()
    yield spark
    spark.stop()
