'use-strict';
const kue = require('kue');
const queue = kue.createQueue();

const queueData = {
  phoneNumber: '9165219225',
  message: 'here is your code'
}

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});  
