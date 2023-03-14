function schoolRegister(input) {
    let students = {};
    let pattern = /\:.[A-Za-z0-9\.]+/mg
    for (const line of input) {
        let [name, grade, score] = line.match(pattern);
        name = name.slice(2);
        grade = Number(grade.slice(2));
        score = Number(score.slice(2));
        if (score >= 3) {
            if (!students.hasOwnProperty(grade)) {
                students[grade] = [[], []];
            }
            students[grade][0].push(name);
            students[grade][1].push(score);
        }
    }

    for (const key in students) {
        let sum = students[key][1].reduce((partialSum, a) => partialSum + a, 0)
        let averageScore = sum / students[key][1].length;
        console.log(`${Number(key) + 1} Grade`)
        console.log(`List of students: ${students[key][0].join(', ')}`)
        console.log(`Average annual score from last year: ${averageScore.toFixed(2)}`)
        console.log()
    }
}

schoolRegister([

    "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
    
    "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
    
    "Student name: George, Grade: 8, Graduated with an average score: 2.83",
    
    "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
    
    "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
    
    "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
    
    "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
    
    "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
    
    "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
    
    "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
    
    "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
    
    "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
    
    ])