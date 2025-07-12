//this program is written to prove that the given algorithm to determine if an integer > 1 is prime or not works

//array of integers from 2 to 1000
let arr = [];
for (let i = 0; i < 999; i++) {
    arr.push((i+2));
}

//prime1 will store prime numbers determined by the algorithm in test, prime2 will store prime numbers determined by our fundamental algorithm 
let prime1 = [], prime2 = [];

//algorithm in test
for(let i = 0; i < arr.length; i++)
{
    if(arr[i] == 2) {
        prime1.push(arr[i]);
    }
    else if (arr[i] % 2 == 0) {
    }
    else {
        let c = 0, t = Math.floor(Math.sqrt(arr[i]));
        for (let j = 2; j <= t; j++){
            if((j % 2 != 0) && (arr[i] % j == 0))
                c++;
        }
        if(c == 0)
            prime1.push(arr[i]);
    }
}

//fundamental algorithm
for (let i = 0; i < arr.length; i++) {
    let c = 0;
    for(let j = 2; j < arr[i]; j++) {
        if (arr[i] % j == 0) {
            c++;
            break;
        }
    }
    if (c == 0)
        prime2.push(arr[i]);
}

//condition to check if the number of prime numbers determined by both algorithm is equal
if (prime1.length == prime2.length) {
    //prints the corresponding elements of both sets of prime numbers determined side by side
    for (let i = 0; i < prime1.length; i++) {
        console.log(prime1[i] + "   " + prime2[i]);
    }
}