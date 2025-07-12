const A = -3,
    B = -2;
let func = (x) => 2 * x * Math.cos(2 * x) - Math.pow(x + 1, 2);

let x,
    fx,
    xn = [];

const sec = (a, b) => {
    x = truncateTo((a * func(b) - b * func(a)) / (func(b) - func(a)), 3);
    xn.push(x);

    console.log(
        xn.length.toString().padStart(4),
        a.toString().padStart(12),
        b.toString().padStart(12),
        x.toString().padStart(12)
    );

    if (xn[xn.length - 2] == xn[xn.length - 1]) {
        console.log(
            "\nThe root is ",
            xn[xn.length - 1].toString(),
            "\n",
            "END"
        );
    } else {
        sec(b, x);
    }
};

sec(A, B);

function truncateTo(num, n) {
    const factor = 10 ** n;
    return Math.trunc(num * factor) / factor;
}
