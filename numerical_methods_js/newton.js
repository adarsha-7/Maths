const x0 = 1;
let func = (x) => Math.pow(Math.E, x) - 4 * x;
let funcf = (x) => Math.pow(Math.E, x) - 4;

const newt = (a) => {
    x = truncateTo(a - func(a) / funcf(a), 4);

    console.log(a.toString().padStart(12), x.toString().padStart(12));
    if (x == a) {
        console.log("\nThe root is ", x);
        return;
    }
    newt(truncateTo(x, 4));
};

console.log("xn".padStart(12), "xn + 1".toString().padStart(12));
newt(x0);

function truncateTo(num, n) {
    const factor = 10 ** n;
    return Math.trunc(num * factor) / factor;
}
