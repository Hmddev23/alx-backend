#!/usr/bin/node
/**
  * This script creates a job queue using Kue, processes jobs in
  * the queue, and sends notifications based on the job data.
  */

import { createQueue } from 'kue';


const queue = createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
