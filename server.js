const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const kafka = require('kafka-node');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Kafka Consumer for processed sales data
const Consumer = kafka.Consumer;
const client = new kafka.KafkaClient({ kafkaHost: 'localhost:9092' });
const consumer = new Consumer(
  client,
  [{ topic: 'processed_sales_topic', partition: 0 }],
  { autoCommit: true }
);

// Listen to Kafka topic and send data to all connected clients
consumer.on('message', function (message) {
  const salesData = JSON.parse(message.value);
  io.emit('salesData', salesData);
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
app.get('/graph.html', (req, res) => {
  res.sendFile(__dirname + '/graph.html');
});

server.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
