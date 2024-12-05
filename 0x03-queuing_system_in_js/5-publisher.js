'use-strict';
import redis from 'redis';
const client = redis.createClient();

const publishMessage = (message, time) => {
  setTimeout(() => {
      console.log(`About to send ${message}`);
      client.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
