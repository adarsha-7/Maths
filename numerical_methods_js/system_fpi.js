const funcx = (x, y) => -0.1 * Math.pow(x, 3) + 0.1 * y + 0.5;
const funcy = (x, y) => 0.1 * x + 0.1 * Math.pow(y, 3) + 0.1;

function fpi(x0, y0) {
    const x1 = truncateTo(funcx(x0, y0), 4);
    const y1 = truncateTo(funcy(x0, y0), 4);

    console.log(x1.toString().padStart(12), y1.toString().padStart(12));
    if (x0 == x1 && y0 == y1) {
        console.log("END");
    } else {
        fpi(x1, y1);
    }
}

fpi(1, 1);

function truncateTo(num, n) {
    const factor = 10 ** n;
    return Math.trunc(num * factor) / factor;
}
