function gethistory () {
    return document.getElementbyId(history-value).innerText;
}
function printhistory(num) {
    document.getElementbyId(history-value).innerText=num;
}
function getoutput() {
    return document.getElementById("output-value").innerText;
}
function printOutput(num) {
    if (num =="") {
        document.getElementById("output-value").innerText = num;
    }
    else {
        document.getElementById("output-value").innerText = getFormattedNumber(num);
    }
}
function getFormattedNumber(num) {
    if (num == "_") {
        return "";
    }
    var n = Number(num);
    var value =n.toLocaleString("en");
    return value;
}
function reverseNumberFormat(num) {
    return Number(num.replace(/ ,/g,''))
}
var operator = document.getElementsByClassName("operator"); 
for (var i =0; i <operator.length; i++) {
    operator{i}.addEventListener('click', function () {})
}