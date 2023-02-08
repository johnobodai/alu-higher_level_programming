#!/usr/bin/node

/* a script that prints My number: <first argument converted in integer> 
 * if the first argument can be converted to an integer:
 */

inputVal = Math.floor(Number(process.argv[2]));
console.log(isNaN(inputVal) ? 'Not a number' : `My number: ${inputVal}`);

