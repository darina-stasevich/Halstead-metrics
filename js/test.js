function functionName1(parameter1, parameter2, parameter3) {
    const x = 42;
    let y = x + 10;
    if (y > 0) {
        console.log("Positive");
    } else if (x < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
}

function functionName2(parameter) {
    switch (parameter) {
        case 1:
            console.log("Case 1");
            break;
        case 2:
            console.log("Case 2");
            break;
        default:
            console.log("Default Case");
    }

    let anotherValue;
    switch (anotherValue) {
        case "A":
            console.log("Case A");
            break;
        case "B":
            console.log("Case B");
            break;
    }
}

function functionName3() {
    // Тело функции
}

function outerFunction() {
    const outerVariable = 10;

    const array = [];
    for (const item of array) {
        console.log(item);
    }

    for (let number = 1; number <= 5; number++) {
        console.log(number);
    }

    const value = 0;
    switch (value) {
        case 1:
            console.log("Case 1");
            break;
        case 2:
            console.log("Case 2");
            break;
        default:
            console.log("Default Case");
    }

    function innerFunction() {
        console.log(`Inside innerFunction, outerVariable is:`);
        console.log(outerVariable)
    }
    innerFunction();

    const result = someFunction("value", 42);
    const anotherResult = anotherFunction();
}

function generateFibonacci(limit) {
    const fibonacciSeries = [];
    let a = 0, b = 1;

    while (a <= limit) {
        fibonacciSeries.push(a);
        const temp = a + b;
        a = b;
        b = temp;
    }

    let c = 0, d = 1;
    while (true) {
        const nextValue = c + d;
        if (nextValue > limit) break;
        fibonacciSeries.push(nextValue);
        c = d;
        d = nextValue;
    }

    const x = 42;
    const y = 3.14;
    const aa = 42;

    return fibonacciSeries;
}

console.log("\n=== Генерация чисел Фибоначчи до 100 ===");
const fibSeries = generateFibonacci(100);
console.log("Ряд Фибоначчи:", fibSeries);

function someFunction(arg1, arg2) {
    return "result";
}

functionName3();