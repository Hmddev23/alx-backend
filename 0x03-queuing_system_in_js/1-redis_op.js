#!/usr/bin/node
/**
  * demonstrate setting up a Redis client using the `redis` library
  * in Node.js, handling events for connection and error logging,
  * and performing basic Redis operations such as setting and
  * getting key-value pairs.
  */

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

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, value) => {
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
