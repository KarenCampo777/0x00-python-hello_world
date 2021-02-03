#!/usr/bin/node

const Message = process.argv.length;
// checks for arguments passed
if (Message === 2) { console.log('No argument'); } else if (Message === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
