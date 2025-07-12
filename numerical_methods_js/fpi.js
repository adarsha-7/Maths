const x0 = 1;
let func = (x) => Math.pow(x + 1, 1 / 3);

let x,
    fx,
    xn = [];

const fpi = (xp) => {
    x = truncateTo(func(xp), 3);
    xn.push(x);

    console.log(
        xn.length.toString().padStart(4),
        xp.toString().padStart(12),
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
        fpi(x);
    }
};

fpi(x0);

function truncateTo(num, n) {
    const factor = 10 ** n;
    return Math.trunc(num * factor) / factor;
}
