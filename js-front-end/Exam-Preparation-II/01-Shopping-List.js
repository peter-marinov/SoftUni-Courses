function shoppingList(input) {
    const shopItems = input.shift().split('!');

    while(input) {
        let line = input.shift();
        if (line === 'Go Shopping!') {
            break;
        }

        
        let [command] = line.split(' ');
 
        if (command === 'Urgent') {
            let [_command, item] = line.split(' ');
            if (!shopItems.includes(item)) {
                shopItems.unshift(item);
            }
        } else if (command === 'Unnecessary') {
            let [_command, item] = line.split(' ');
            if (shopItems.includes(item)) {
                let index = shopItems.indexOf(item);
                shopItems.splice(index, 1);
            }
        } else if (command === 'Correct') {
            let [_command, oldItem, newItem] = line.split(' ');
            if (shopItems.includes(oldItem)) {
                let index = shopItems.indexOf(oldItem);
                shopItems.splice(index, 1, newItem);
            }
        } else if (command === 'Rearrange') {
            let [_command, item] = line.split(' ');
            if (shopItems.includes(item)) {
                let index = shopItems.indexOf(item);
                let movedItem = shopItems.splice(index, 1);
                shopItems.push(movedItem)
            }
        }
    }

    console.log(shopItems.join(', '))
}

shoppingList(["Tomatoes!Potatoes!Bread",
"Unnecessary Milk",
"Urgent Tomatoes",
"Go Shopping!"]);