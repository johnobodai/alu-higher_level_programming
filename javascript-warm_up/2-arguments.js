#!/usr/bin/node

const readline = require("argument");

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
