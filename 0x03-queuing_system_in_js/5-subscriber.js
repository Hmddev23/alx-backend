#!/usr/bin/node
/**
  * connect to a Redis server, subscribes to a Redis channel,
  * and listens for messages on that channel. If a specific
  * message is received, it unsubscribes from the channel
  * and quits the client.
  */

import { createClient } from 'redis';


const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const listener = (message) => console.log(message);

client.SUBSCRIBE('holberton school channel');

client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      client.UNSUBSCRIBE();
      client.QUIT();
    }
    listener(message);
  }
});
