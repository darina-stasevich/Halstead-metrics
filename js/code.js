function is_odd(num) {
    if (num & 1) {
        return true;
    } else {
        return false;
    }
}

for (var i = 1; i < 100; i++) {
    document.write(i + ": " + is_odd(i) + "<br>");
}
