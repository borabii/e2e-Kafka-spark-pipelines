# Realtime Data Streaming & Containerized Data Engineering: End-to-End Pipelines with Apache Airflow, Kafka, Spark, and Cassandra

## Introduction

This project is about building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. Everything is containerized using Docker for ease of deployment and scalability.

## System Architecture

The project is designed with the following components:

- **Data Source**: We use `randomuser.me` API to generate random user data for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.

## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/borabii/e2e-Kafka-spark-pipelines
   ```

2. Navigate to the project directory:

   ```bash
   cd e2e-Kafka-spark-pipelines
   ```

3. Run Docker cp to copy the spark code to the spark container:

   ```bash
   docker cp .\spark_stream.py <spark-container-id>:/opt/bitnami/spark/spark-apps/spark_stream.py
   ```

4. Run Docker exec to subpit the code to the spark-master:
   ```bash
   docker exec -it d97 spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/spark-apps/spark_connection.py
   ```
