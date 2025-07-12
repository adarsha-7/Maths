const A = -3,
    B = -2;
let func = (x) => 2 * x * Math.cos(2 * x) - Math.pow(x + 1, 2);

let x,
    fx,
    xn = [];

const falp = (a, b) => {
    x = truncateTo((a * func(b) - b * func(a)) / (func(b) - func(a)), 3);
    fx = truncateTo(func(x), 3);
    xn.push(x);

    console.log(
        xn.length.toString().padStart(4),
        a.toString().padStart(12),
        b.toString().padStart(12),
        x.toString().padStart(12),
        (Math.sign(fx) == -1 ? "-ve" : "+ve").padStart(6)
    );

    if (xn[xn.length - 2] == xn[xn.length - 1]) {
        console.log(
            "\nThe root is ",
            xn[xn.length - 1].toString(),
            "\n",
            "END"
        );
    } else if (fx * func(a) > 0) {
        falp(x, truncateTo(b, 3));
    } else if (fx * func(a) < 0) {
        falp(truncateTo(a, 3), x);
    } else {
        console.log(
            "\nThe root is ",
            xn[xn.length - 1].toString(),
            "\n",
            "END"
        );
    }
};

falp(A, B);

function truncateTo(num, n) {
    const factor = 10 ** n;
    return Math.trunc(num * factor) / factor;
}
