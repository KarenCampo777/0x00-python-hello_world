#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  const users = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
