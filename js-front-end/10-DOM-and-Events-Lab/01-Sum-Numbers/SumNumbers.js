function calc() {
    const firstInput = document.getElementById('num1');
    const secondInput = document.getElementById('num2');
    const sumInput = document.getElementById('sum');

    let firstNum = Number(firstInput.value);
    let secondNum = Number(secondInput.value);
    sumInput.value = firstNum + secondNum;
}
