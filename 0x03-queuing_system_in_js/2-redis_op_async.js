#!/usr/bin/node
/**
  * set up a Redis client using the `redis` library in Node.js,
  * handles events for connection and error logging, and performs
  * basic Redis operations such as setting and getting key-value pairs.
  * It demonstrate the use of Promises to handle asynchronous operations.
  */

import { promisify } from 'util';
import { createClient, print } from 'redis';


const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const GET = promisify(client.GET).bind(client);
  try {
    const value = await GET(schoolName);
    console.log(value);
  } catch (error) {
    console.log(error.toString());
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
