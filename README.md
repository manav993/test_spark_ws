
# Real-Time Sales Dashboard

This project is a real-time sales dashboard application that visualizes sales data using various technologies. It includes a producer that generates sales data, a Spark application for processing and publishing the data, and a Node.js server that serves a web interface and provides real-time updates.

## Technologies Used

- **Apache Kafka**: A distributed streaming platform used for managing and processing streaming data. Kafka topics are used to publish and subscribe to sales data.
- **Apache Spark**: A unified analytics engine for large-scale data processing. Spark processes the incoming sales data and publishes it to a new Kafka topic.
- **Node.js**: A JavaScript runtime built on Chrome's V8 engine. It runs a server that serves the web interface and uses Kafka's node client to consume processed sales data.
- **Socket.IO**: A library for real-time web applications. It enables real-time, bi-directional communication between the Node.js server and the web browser.
- **Express**: A web application framework for Node.js. It is used to handle HTTP requests and serve the static files for the web interface.
- **HTML/CSS**: Used for creating the web pages and styling them. The pages include a table for displaying real-time sales data and a separate page with a graph (which is currently not in focus).
- **JavaScript**: For dynamic content updates on the web pages using Socket.IO.

## How It Works

1. **Producer**:
   - The Kafka producer generates random sales data and sends it to a Kafka topic named `sales_topic_electronics`.
   - The data includes product type, quantity, and price.

2. **Spark Application**:
   - The Spark application reads the sales data from the `sales_topic_electronics` Kafka topic.
   - It processes the data and writes the processed sales data to a new Kafka topic named `processed_sales_topic`.

3. **Node.js Server**:
   - The Node.js server runs an Express application and uses the Kafka node client to consume messages from the `processed_sales_topic`.
   - It uses Socket.IO to push new sales data to connected clients in real time.
   - The server serves two pages:
     - **index.html**: Displays real-time sales data in a table format. The table updates dynamically as new sales data arrives.
     - **graph.html**: Intended to show a real-time graph of sales data (currently not in focus).

4. **Web Interface**:
   - The `index.html` page shows a table with columns for product name, total quantity, and total price. It updates dynamically with real-time data.
   - The `graph.html` page (if implemented) would visualize sales data using a graph.

## How to Run the Application

1. **Start Kafka and Zookeeper**:
   - Ensure Kafka and Zookeeper are running on your local machine.

2. **Run the Spark Application**:
   - Ensure you have Spark installed and configured.
   - Submit the Spark job to process the Kafka data.

3. **Start the Kafka Producer**:
   - Run the Kafka producer script to start sending sales data.

4. **Start the Node.js Server**:
   - Ensure Node.js is installed.
   - Install dependencies: `npm install`
   - Start the server: `node server.js`

5. **Access the Web Interface**:
   - Open a web browser and navigate to `http://localhost:3000` to view the real-time sales data.
   - Navigate to `http://localhost:3000/graph.html` for the graph page (if implemented).

## Notes

- Ensure all Kafka topics are created and correctly named.
- Ensure that the Kafka brokers, Zookeeper, and Spark configurations match the settings used in the application.
- The graph functionality is currently not implemented, but it can be integrated based on your requirements.
