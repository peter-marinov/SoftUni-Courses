function solve(input) {
    const iterations = Number(input.shift());
    let assigneesDB = {};
    let toDoTasksTotalPoints = 0;
    let inProgressTasksTotalPoints = 0;
    let codeReviewTasksTotalPoints = 0;
    let doneTasksTotalPoints = 0;

    for (let i = 0; i < iterations; i++) {
        const line = input.shift();
        const [assignee, taskId, title, status, estimatedPoints] = line.split(':');
        if (assignee in assigneesDB) {
            let a = 0;
        } else {
            assigneesDB[assignee] = {};
        }
        assigneesDB[assignee][taskId] = { title, status, estimatedPoints }
    }

    while (input.length > 0) {
        const commandLine = input.shift();
        const [command] = commandLine.split(':');

        if (command === 'Add New') {
            const [_command, assignee, taskId, title, status, estimatedPoints] = commandLine.split(':');
            if (assignee in assigneesDB) {
                assigneesDB[assignee][taskId] = { title, status, estimatedPoints }
            } else {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            }
        } else if (command === 'Change Status') {
            const [_command, assignee, taskId, newStatus] = commandLine.split(':');
            if (!assigneesDB.hasOwnProperty(assignee)) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
                continue;
            }
            if (!assigneesDB[assignee].hasOwnProperty(taskId)) {
                console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
                continue;
            }
            assigneesDB[assignee][taskId].status = newStatus;

        } else if (command === 'Remove Task') {
            const [_command, assignee, index] = commandLine.split(':');
            if (!assigneesDB.hasOwnProperty(assignee)) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
                continue;
            }
            const keys = Object.keys(assigneesDB[assignee]);
            if (index < 0 || index >= keys.length) {
                console.log("Index is out of range!");
                continue;
            }
            delete assigneesDB[assignee][keys[index]];
        }
    }

    for (person in assigneesDB) {
        for (task in assigneesDB[person]) {
            if (assigneesDB[person][task].status === 'ToDo') {
                toDoTasksTotalPoints += Number(assigneesDB[person][task].estimatedPoints);
            } else if (assigneesDB[person][task].status === 'In Progress') {
                inProgressTasksTotalPoints += Number(assigneesDB[person][task].estimatedPoints);
            } else if (assigneesDB[person][task].status === 'Code Review') {
                codeReviewTasksTotalPoints += Number(assigneesDB[person][task].estimatedPoints);
            } else if (assigneesDB[person][task].status === 'Done') {
                doneTasksTotalPoints += Number(assigneesDB[person][task].estimatedPoints);
            }
        }
    }

    console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
    console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
    console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
    console.log(`Done Points: ${doneTasksTotalPoints}pts`);

    if (doneTasksTotalPoints >= (toDoTasksTotalPoints + inProgressTasksTotalPoints + codeReviewTasksTotalPoints)) {
        console.log('Sprint was successful!')
    } else {
        console.log('Sprint was unsuccessful...')
    }
}
    solve([
        '5',
        'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
        'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
        'Peter:BOP-1211:POC:Code Review:5',
        'Georgi:BOP-1212:Investigation Task:Done:2',
        'Mariya:BOP-1213:New Account Page:In Progress:13',
        'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
        'Change Status:Peter:BOP-1290:ToDo',
        'Remove Task:Mariya:1',
        'Remove Task:Joro:1',
    ]);