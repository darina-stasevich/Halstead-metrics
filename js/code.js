function is_odd(num) {
    if (num & 1) {
        return true;
    } else {
        return false;
    }
}

for (var i = 1; i < 100; i++) {
    if (i % 10 === 0) continue;
    document.write(i + ":: " + is_odd(i) + "<br>");
    document.write((((2 + ((2 > i) ? 5 : 9)) / 5) * (2 * 6 - 3)));
}

let a = 2 + 2;

switch (a) {
    case 3:
        alert('Маловато');
        break;
    case 4:
        alert('В точку!');
        break;
    case 5:
        alert('Перебор');
        break;
    default:
        alert("Нет таких значений");
}

const arr = [1, 2, 3];
for (let value of arr) {
    if (value === 2) break;
    console.log(value);
}

var c = null;
var b = undefined;

const obj = new Object();
obj.name = "Example";

console.log(obj instanceof Object); // true

console.log("name" in obj); // true
console.log("age" in obj);  // false

console.log(typeof obj);   // object
console.log(typeof b);     // undefined
console.log(typeof 42);    // number
console.log(typeof "Hi");  // string

delete obj.name;
console.log("name" in obj); // false

class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log("издает звук");
    }
}