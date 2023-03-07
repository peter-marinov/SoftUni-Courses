function solve(fruit, weight, price) {
    let kilograms =  weight / 1000 
    let money = price * kilograms
    console.log(`I need $${money.toFixed(2)} to buy ${kilograms.toFixed(2)} kilograms ${fruit}.`)
}

solve('orange', 2500, 1.80)