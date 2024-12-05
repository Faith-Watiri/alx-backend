'use-strict';
import redis from 'redis';
const client = redis.createClient();

client.subscribe("holberton school channel");

client.on('message', (channel, message) => {
  console.log(message);
  if (message == 'KILL_SERVER') {
    client.unsubscribe(channel);
    process.exit(0);
  }
});
