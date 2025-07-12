const A = 0.5,
    B = 1;
let func = (x) => Math.pow(x, 2) - Math.sin(x);

let x,
    fx,
    xn = [];

const bisc = (a, b) => {
    x = truncateTo((a + b) / 2, 4);
    fx = truncateTo(func(x), 4);
    xn.push(x);

    console.log(
        xn.length.toString().padStart(4),
        a.toString().padStart(12),
        b.toString().padStart(12),
        x.toString().padStart(12),
        (Math.sign(fx) == -1 ? "-ve" : "+ve").padStart(6)
    );

    if (xn[xn.length - 2] == xn[xn.length - 1] || fx == 0) {
        console.log("END");
    } else if (fx < 0) {
        bisc(x, truncateTo(b, 4));
    } else if (fx > 0) {
        bisc(truncateTo(a, 4), x);
    }
};

bisc(A, B);

function truncateTo(num, n) {
    const factor = 10 ** n;
    return Math.trunc(num * factor) / factor;
}
