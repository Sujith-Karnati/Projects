let display = document.getElementById("display");

function appendNumber(num) {
    display.value += num;
}

function appendOperator(operator) {
    display.value += " " + operator + " ";
}

function clearDisplay() {
    display.value = "";
}

function calculateResult() {
    try {
        display.value = eval(display.value);
    } catch (e) {
        display.value = "Error";
    }
}
