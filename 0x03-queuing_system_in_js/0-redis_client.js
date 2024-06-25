#!/usr/bin/node
/**
  * set up a Redis client using the `redis` library in Node.js.
  */

import { createClient } from 'redis';


const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
