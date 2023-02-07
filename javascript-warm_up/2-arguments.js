#!/usr/bin/node

// const readline = require("argument");
/*
const argument = process.argv
function arg(argument){
    if (arguments.length > 0){
        if (arguments.length == 1){
            return ('Argument found');            
        }else{
            return ('Arguments found');
        }
    }else{
       return ('No argument');
    }
}

console.log(arg())
*/

const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
