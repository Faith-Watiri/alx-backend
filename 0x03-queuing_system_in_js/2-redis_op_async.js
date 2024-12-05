'use strict';
import redis from 'redis';
const client = redis.createClient();
const promisedData = promisify(client.get).bind(client);

client.on("error", (err) => {
  if (err) console.log(`Redis client not connected to the server: ${err}`)
}).on('ready', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

const  displaySchoolValue = async (schoolName) => {
  const data = await promisedData(schoolName)
    console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
