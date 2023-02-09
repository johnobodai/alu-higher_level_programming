#!/usr/bin/node

/* A script that searches the second 
 * biggest integer in the lost of 
 * argument
 */

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
