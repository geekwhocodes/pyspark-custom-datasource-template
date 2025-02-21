# Apache PySpark Custom Data Source Template

This repository provides a template for creating a custom data source for Apache PySpark. It is designed to help developers extend PySpark’s data source API to support custom data ingestion and storage mechanisms.


## Motivation

When developing custom PySpark data sources, I encountered several challenges that made the development process frustrating:

1. **Environment Setup Complexity**: Setting up a development environment for PySpark data source development was unnecessarily complex, with multiple dependencies and version conflicts.

2. **Test Data Management**: Managing test data and maintaining consistent test environments across different machines was challenging.

3. **Debugging Issues**: The default setup made it difficult to debug custom data source code effectively, especially when dealing with Spark's distributed nature.

4. **Documentation Gaps**: Existing documentation for custom data source development was scattered and often incomplete.

This template repository aims to solve these pain points and provide a streamlined development experience.


## Features

- Pre-configured development environment
- Ready-to-use test infrastructure
- Example implementation
- Automated tests setup
- Debug-friendly configuration

## Getting Started

Follow these steps to set up and use this repository:

### Prerequisites

- Docker
- Visual Studio Code
- Python 3.11

### Creating a Repository from This Template

To create a new repository based on this template:

1. Go to the [GitHub repository](https://github.com/geekwhocodes/pyspark-custom-datasource-template).
2. Click the **Use this template** button.
3. Select **Create a new repository**.
4. Choose a repository name, visibility (public or private), and click **Create repository from template**.
5. Clone your new repository:

    ```sh
    git clone https://github.com/your-username/your-new-repository.git
    cd your-new-repository
    ```

### Setup

1. **Open the repository in Visual Studio Code:**

    ```sh
    code .
    ```

2. **Build and start the development container:**

    Open the command palette (Ctrl+Shift+P) and select `Remote-Containers: Reopen in Container`.

3. **Initialize the environment:**

    The environment will be initialized automatically by running the `init-env.sh` script defined in the `devcontainer.json` file.

### Project Structure

The project follows this structure:

```
.
├── src/
│   ├── fake_source/         # Default fake data source implementation
│   │   ├── __init__.py
│   │   ├── source.py        # Implementation of the fake data source
│   │   ├── schema.py        # Schema definitions (if applicable)
│   │   └── utils.py         # Helper functions (if needed)
│   ├── tests/               # Unit tests for the custom data source
│   │   ├── __init__.py
│   │   ├── test_source.py   # Tests for the data source
│   │   └── conftest.py      # Test configuration and fixtures
├── .devcontainer/           # Development container setup files
│   ├── Dockerfile
│   ├── devcontainer.json
├── |── scripts
├── |   ├── init-env.sh              # Initialization script for setting up the environment
├── pyproject.toml           # Project dependencies and build system configuration
├── README.md                # Project documentation
├── LICENSE                  # License file
```

### Usage

By default, this template includes a **fake data source** that generates mock data. You can use it as-is or replace it with your own implementation.

1. **Register the custom data source:**

    ```python
    from pyspark.sql import SparkSession
    from fake_source.source import FakeDataSource

    spark = SparkSession.builder.getOrCreate()
    spark.dataSource.register(FakeDataSource)
    ```

2. **Read data using the custom data source:**

    ```python
    df = spark.read.format("fake").load()
    df.show()
    ```

3. **Run tests:**

    ```sh
    pytest
    ```

### Customization

To replace the fake data source with your own:

1. **Rename the package folder:**

    ```sh
    mv src/fake_source src/your_datasource_name
    ```

2. **Update imports in `source.py` and other files:**

    ```python
    from your_datasource_name.source import CustomDataSource
    ```

3. **Update `pyproject.toml` to reflect the new package name.**

4. **Modify the schema and options in `source.py` to fit your use case.**

### References
1. [Microsoft Learn - PySpark custom data sources](https://learn.microsoft.com/en-us/azure/databricks/pyspark/datasources)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For issues and questions, please use the GitHub Issues section.


### Need Help Setting Up a Data Intelligence Platform with Databricks?
If you need expert guidance on setting up a modern data intelligence platform using Databricks, we can help. Our consultancy specializes in:

- Custom data source development for Databricks and Apache Spark
- Optimizing ETL pipelines for performance and scalability
- Data governance and security using Unity Catalog
- Building ML & AI solutions on Databricks

🚀 [Contact us](https://www.linkedin.com/in/geekwhocodes/) for a consultation and take your data platform to the next level.
