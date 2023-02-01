#!/usr/bin/node

function arg(argument){
    if (arguments.length > 0){
        if (arguments.length == 1){
            console.log('Argument found');            
        }else{
            console.log('Arguments found');
        }
    }else{
        console.log('No argument');
    }
}

arg('af,adf')
