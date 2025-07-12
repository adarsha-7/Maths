const x = [0, 1, 3, 4, 5];
const y = [0, 1, 81, 256, 625];
const a = 2;

function l(i) {
    let v = 1;
    for (j = 0; j < x.length; j++) {
        if (i != j) {
            v *= (a - x[j]) / (x[i] - x[j]);
        }
    }
    return v;
}

let fx = 0;
for (let i = 0; i < x.length; i++) {
    fx += l(i) * y[i];
}

console.log(`Using Lagrange Interpolation, f(${a}) = ${fx}`);
