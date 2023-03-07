function passwordValidator(password) {
    let isValid = true;
    let patternLettersNumbers = /^[A-Za-z0-9]*$/gm;
    let patternAtLeastTwoDigits = /[0-9]{2,}/gm;

    if (password.length < 6 || password.length > 10) {
        isValid = false;
        console.log("Password must be between 6 and 10 characters");
    }

    if (password.match(patternLettersNumbers) === null){
        isValid = false;
        console.log("Password must consist only of letters and digits");
    }

    if (password.match(patternAtLeastTwoDigits) === null) {
        isValid = false;
        console.log("Password must have at least 2 digits");
    }

    if (isValid === true) {
        console.log("Password is valid");
    }
}

passwordValidator('logIn')