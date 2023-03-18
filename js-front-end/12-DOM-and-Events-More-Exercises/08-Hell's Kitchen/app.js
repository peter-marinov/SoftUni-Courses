function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      const textArea = document.getElementsByTagName('textarea')[0];
      const bestRestaurant = document.querySelector('#bestRestaurant > p');
      const bestRestaurantWorkers = document.querySelector('#workers > p');
      let restaurantsArray = textArea.
         value
         .slice(2, textArea.value.length - 2);
      if (restaurantsArray.includes('", "')) {
         restaurantsArray = restaurantsArray.split('", "');
      } else {
         restaurantsArray = restaurantsArray.split('","');
      }
         


      let restaurantsDB = {};
      let restaurantSalaries = [];

      for (const restaurant of restaurantsArray) {
         let [restaurantName, workers] = restaurant.split(' - ');
         let allSalaries = 0;
         let averageSalary = 0;
         if (!restaurantsDB.hasOwnProperty(restaurantName)) {
            restaurantsDB[restaurantName] = {};
         }

         workers = workers.split(', ');

         for (const worker of workers) {
            let [workerName, workerSalary] = worker.split(' ');
            workerSalary = Number(workerSalary);
            restaurantsDB[restaurantName][workerName] = workerSalary;
            allSalaries += workerSalary
         }

         averageSalary = Number(allSalaries / workers.length);
         // restaurantsDB[restaurantName]['totalSalary'] = allSalaries.toFixed(2);
         restaurantsDB[restaurantName]['averageSalary'] = averageSalary.toFixed(2);
         
      }
      
      for (const key in restaurantsDB) {
         restaurantSalaries.push([key, restaurantsDB[key]['averageSalary']]);
      }
      
      // let 
      let sortedRestaurantSalaries = restaurantSalaries.sort((a, b) => b[1] - a[1]);
      let sortedSalaries = [];
      for (const worker in restaurantsDB[sortedRestaurantSalaries[0][0]]) {
         if (worker !== 'totalSalary' && worker !== 'averageSalary') {
            sortedSalaries.push([worker, restaurantsDB[sortedRestaurantSalaries[0][0]][worker]]);
         }
      }
      console.log(sortedRestaurantSalaries)
      console.log(restaurantsDB)
      console.log(sortedSalaries)
      sortedSalaries = sortedSalaries.sort((a, b) => b[1] - a[1])
      

      bestRestaurant.textContent = `Name: ${sortedRestaurantSalaries[0][0]} Average Salary: ${sortedRestaurantSalaries[0][1]} Best Salary: ${sortedSalaries[0][1].toFixed((2))}`;

      let result = [];
  
      for (const worker of sortedSalaries) {
         let [workerName, workerSalary] = worker;
         result.push([` Name: ${workerName} With Salary: ${workerSalary}`]);
      }
      
      bestRestaurantWorkers.textContent = result.join('');
   }
}