#!/usr/bin/node

/*
 * The process.argv property returns an array containing the arguments passed
 * to the process when run in the command line. The first element is the process
 * execution path and the second element is the path for the js file. Hence 
 * the need to start the count from two and not 0.
*/

const argument = process.argv.length;
console.log(argument === 2 ? 'No argument' : argument === 3 ? 'Argument found' : 'Arguments found');
