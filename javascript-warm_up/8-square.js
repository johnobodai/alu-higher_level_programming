#!/usr/bin/node

const integerNum = Math.floor(Number(process.argv[2]));
if (isNaN(integerNum)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < integerNum; r++) {
    let row = '';
    for (let c = 0; c < integerNum; c++) {
      row += 'X';
    }
        console.log(row);
  }
}
