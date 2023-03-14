function convertToObject(jsonStr) {
    let person = JSON.parse(jsonStr);
    
    const information = Object.entries(person);
    for (const [key, value] of information) {
        console.log(`${key}: ${value}`);
    }
    
}

convertToObject('{"name": "George", "age": 40, "town": "Sofia"}')