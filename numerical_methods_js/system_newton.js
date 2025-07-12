const x = 2,
    y = 2;

const f = Math.pow(x, 2) - 3 * x * y + 7;
const g = y - 2 * x - 2;
const fx = 2 * x - 3 * y;
const fy = -3 * x;
const gx = -2;
const gy = 1;
const d = fx * gy - fy * gx;
const d1 = fy * g - f * gy;
const d2 = f * gx - fx * g;

console.log(x, y, f, g, fx, fy, gx, gy, d, d1, d2, d1 / d, d2 / d);
