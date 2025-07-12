const f = (x) => Math.exp(x);
const a = -1,
    b = 1,
    h = 0.1;

let x = [];
x.push(a);
while (true) {
    const current_value = +(x[x.length - 1] + h).toFixed(4);
    if (current_value <= b) x.push(current_value);
    else break;
}

let y = [];
for (let i = 0; i < x.length; i++) {
    y.push(+f(x[i]).toFixed(4));
}

let header = "x".padStart(8) + "y".padStart(8);
for (let i = 1; i < x.length; i++) {
    header += ("del" + i.toString()).padStart(8);
}
console.log(header);

const values = [];
for (let i = 0; i < x.length - 1; i++) {
    values[i] = [];
    for (let j = 0; j < x.length - i - 1; j++) {
        if (i === 0) {
            values[i][j] = +(y[j + 1] - y[j]).toFixed(4);
        } else {
            values[i][j] = +(values[i - 1][j + 1] - values[i - 1][j]).toFixed(
                4
            );
        }
    }
}

for (let i = 0; i < x.length; i++) {
    let row = x[i].toString().padStart(8) + y[i].toString().padStart(8);
    for (let j = 0; j < x.length - 1 - i; j++) {
        row += values[j][i].toFixed(4).toString().padStart(8);
    }
    console.log(row);
}
