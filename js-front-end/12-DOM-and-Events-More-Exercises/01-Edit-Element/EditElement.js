function editElement(element, stringToReplace, newString) {
    while (element.textContent.includes(stringToReplace)) {
        element.textContent = element.textContent.replace(stringToReplace, newString);
    }
}