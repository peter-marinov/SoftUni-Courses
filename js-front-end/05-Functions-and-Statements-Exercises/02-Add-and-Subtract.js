function addAndSubtract(firstNum, secondNum, thirdNum) {
    function add(firstNum, secondNum) {
        return firstNum + secondNum;
    }

    function subtract(firstNum, secondNum, thirdNum){
        return add(firstNum, secondNum) - thirdNum;
    }

    return subtract(firstNum, secondNum, thirdNum);
}

console.log(addAndSubtract(23, 6, 10))