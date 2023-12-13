/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

const n = parseInt(readline()); // the number of temperatures to analyse
var inputs = readline().split(' ');
res = -Infinity
for (let i = 0; i < n; i++) {
    const t = parseInt(inputs[i]);// a temperature expressed as an integer ranging from -273 to 5526
    if(Math.abs(t) < Math.abs(res)) {
        res = t;
    } else if(Math.abs(t) == Math.abs(res)) {
        res = Math.max(t, res);
    } else {
        continue;
    }
}

// Write an answer using console.log()
// To debug: console.error('Debug messages...');
if(res === -Infinity) {
    res = 0
}
console.log(res);
