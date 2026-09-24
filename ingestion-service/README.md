# Ingestion Service

The ingestion service collects real-time rainfall and water-sensor data for the Urban Flood Nowcasting System.

## Responsibilities

- Receive water-sensor data through MQTT
- Process and validate incoming sensor data
- Receive rainfall/radar data
- Send processed events to Apache Kafka
- Provide reliable data for the flood prediction pipeline

## Data Flow

Water Sensors
↓
MQTT Broker
↓
sensor_listener.py
↓
Kafka Producer
↓
Apache Kafka
↓
Flood Prediction System

## Main Files

- `app/sensor_listener.py` - Receives water-sensor data through MQTT
- `app/kafka_producer.py` - Sends events to Apache Kafka
- `app/radar_consumer.py` - Processes rainfall/radar data
- `app/schemas.py` - Defines data structures
- `app/config.py` - Stores application configuration

## Technologies

- Python
- MQTT
- Apache Kafka
- NetCDF
- JSON
