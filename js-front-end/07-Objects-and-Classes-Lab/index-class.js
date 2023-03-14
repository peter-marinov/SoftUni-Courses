class Student {
    constructor(name, age, grades) {
        this.name = name;
        this.age = age;
        this.grades = grades;
    }

    sayHello() {
        console.log(`My name is ${this.name}`)
    }
}

const student1 = new Student('Kiril', 25, [3,4,5]);
const student2 = new Student('Georgi', 26, [4,4,5]);
const student3 = new Student('Peter', 27, [6,5,4]);

student1.sayHello();