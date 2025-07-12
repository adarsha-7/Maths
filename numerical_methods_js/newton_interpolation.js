const x = [0.2, 0.22, 0.24, 0.26, 0.28, 0.3];
const y = [1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139];

const a = 0.21,
    b = 0.29;

function factorial(a) {
    let f = 1;
    for (let i = 1; i <= a; i++) {
        f *= i;
    }
    return f;
}

const values = [];
for (let i = 0; i < y.length - 1; i++) {
    values[i] = [];
    for (let j = 0; j < y.length - i - 1; j++) {
        if (i === 0) {
            values[i][j] = +(y[j + 1] - y[j]).toFixed(4);
        } else {
            values[i][j] = +(values[i - 1][j + 1] - values[i - 1][j]).toFixed(
                4
            );
        }
    }
}

console.log("Difference Table:");

for (let i = 0; i < y.length; i++) {
    let row = x[i].toString().padStart(8) + y[i].toString().padStart(8);
    for (let j = 0; j < x.length - 1 - i; j++) {
        row += values[j][i].toFixed(4).toString().padStart(8);
    }
    console.log(row);
}

let fa = y[0];
let pa = (a - x[0]) / (x[1] - x[0]);

for (let i = 0; i < values.length; i++) {
    let current = values[i][0] / factorial(i);
    for (let j = 0; j < i + 1; j++) {
        current *= pa - j;
    }
    fa += current;
}

console.log("Newton's forward interpolation: Value at x=", a, "is", fa);

let n = x.length - 1;
let fb = y[n];
let pb = (b - x[n]) / (x[1] - x[0]);

for (let i = 0; i < values.length; i++) {
    let current = values[i][n - 1 - i] / factorial(i);
    for (let j = 0; j < i + 1; j++) {
        current *= pb + j;
    }
    fb += current;
}
console.log("Newton's backward interpolation: Value at x=", b, "is", fb);
