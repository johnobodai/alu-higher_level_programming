#!/usr/bin/node

console.log(process.argv.length === 4 ? process.argv[3] 'is' process.argv[4] : process.argv.length === 3 ? process.argv[3] 'is undefined' : 'undefined is undefined' )
