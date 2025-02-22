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
    // Первый switch (предполагаем, что value должен быть parameter)
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

    // Второй switch (anotherValue не определён - оставлен как пример)
    let anotherValue; // Предполагаем, что переменная существует
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

    // Цикл по массиву (предполагаем, что array существует)
    const array = []; // Пример инициализации
    for (const item of array) {
        console.log(item);
    }

    // Цикл по диапазону 1-5
    for (let number = 1; number <= 5; number++) {
        console.log(number);
    }

    // Switch (предполагаем, что value существует)
    const value = 0; // Пример значения
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
        console.log(`Inside innerFunction, outerVariable is ${outerVariable}`);
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

// ... предыдущие функции остаются без изменений ...

// Добавляем вызовы функций в конце
console.log("=== Запуск functionName1 ===");
functionName1("test", 2, true);

console.log("\n=== Запуск functionName2 ===");
functionName2(2);
functionName2(5);

console.log("\n=== Запуск outerFunction ===");
outerFunction();

console.log("\n=== Генерация чисел Фибоначчи до 100 ===");
const fibSeries = generateFibonacci(100);
console.log("Ряд Фибоначчи:", fibSeries);

// Дополнительные функции-заглушки для демонстрации
function someFunction(arg1, arg2) {
    console.log(`someFunction вызвана с параметрами: ${arg1}, ${arg2}`);
    return "result";
}

function anotherFunction() {
    console.log("anotherFunction вызвана");
    return 42;
}

console.log("\n=== Запуск functionName3 ===");
functionName3();