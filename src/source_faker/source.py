from pyspark.sql.datasource import DataSource, DataSourceReader
from pyspark.sql.types import StructType, StringType

# Reference https://learn.microsoft.com/en-us/azure/databricks/pyspark/datasources


class FakeDataSource(DataSource):
    """
    A fake data source for PySpark to generate synthetic data using the `faker` library.

    This data source allows specifying a schema with field names that correspond to `faker`
    providers to generate random data for testing and development purposes.

    The default schema is `name string, date string, zipcode string, state string`, and the
    default number of rows is `3`. Both can be customized by users.

    Name: `fake`

    Notes
    -----
    - The fake data source relies on the `faker` library. Make sure it is installed and accessible.
    - Only string type fields are supported, and each field name must correspond to a method name in
      the `faker` library.

    Examples
    --------
    Register the data source.

    >>> from pyspark_datasources import FakeDataSource
    >>> spark.dataSource.register(FakeDataSource)

    Use the fake datasource with the default schema and default number of rows:

    >>> spark.read.format("fake").load().show()
    +-----------+----------+-------+-------+
    |       name|      date|zipcode|  state|
    +-----------+----------+-------+-------+
    |Carlos Cobb|2018-07-15|  73003|Indiana|
    | Eric Scott|1991-08-22|  10085|  Idaho|
    | Amy Martin|1988-10-28|  68076| Oregon|
    +-----------+----------+-------+-------+

    Use the fake datasource with a custom schema:

    >>> spark.read.format("fake").schema("name string, company string").load().show()
    +---------------------+--------------+
    |name                 |company       |
    +---------------------+--------------+
    |Tanner Brennan       |Adams Group   |
    |Leslie Maxwell       |Santiago Group|
    |Mrs. Jacqueline Brown|Maynard Inc   |
    +---------------------+--------------+

    Use the fake datasource with a different number of rows:

    >>> spark.read.format("fake").option("numRows", 5).load().show()
    +--------------+----------+-------+------------+
    |          name|      date|zipcode|       state|
    +--------------+----------+-------+------------+
    |  Pam Mitchell|1988-10-20|  23788|   Tennessee|
    |Melissa Turner|1996-06-14|  30851|      Nevada|
    |  Brian Ramsey|2021-08-21|  55277|  Washington|
    |  Caitlin Reed|1983-06-22|  89813|Pennsylvania|
    | Douglas James|2007-01-18|  46226|     Alabama|
    +--------------+----------+-------+------------+
    """

    @classmethod
    def name(cls):
        return "fake"

    def schema(self):
        return "name string, date string, zipcode string, state string"

    def reader(self, schema: StructType):
        # Verify the library is installed correctly.
        try:
            from faker import Faker
        except ImportError:
            raise Exception(
                "You need to install `faker` to use the fake datasource.")

        # Check the schema is valid before proceed to reading.
        fake = Faker()
        for field in schema.fields:
            try:
                getattr(fake, field.name)()
            except AttributeError:
                raise Exception(
                    f"Unable to find a method called `{field.name}` in faker. "
                    f"Please check Faker's documentation to see supported methods."
                )
            if field.dataType != StringType():
                raise Exception(
                    f"Field `{field.name}` is not a StringType. "
                    f"Only StringType is supported in the fake datasource."
                )

        return FakeDataSourceReader(schema, self.options)


class FakeDataSourceReader(DataSourceReader):

    def __init__(self, schema, options):
        self.schema: StructType = schema
        self.options = options

    def read(self, partition):
        from faker import Faker
        fake = Faker()
        # Note: every value in this `self.options` dictionary is a string.
        num_rows = int(self.options.get("numRows", 3))
        for _ in range(num_rows):
            row = []
            for field in self.schema.fields:
                value = getattr(fake, field.name)()
                row.append(value)
            yield tuple(row)
