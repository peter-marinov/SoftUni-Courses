function search() {
   const towns = Array.from(document.querySelectorAll('#towns > li'));
   const searchedText = document.getElementById('searchText');
   const result = document.getElementById('result');
   let selectedTowns = [];
   for (const town of towns) {
      town.style.fontWeight = '';
      town.style.textDecoration = '';
   }

   
   if (searchedText.value.trim() !== '') {
      for (const town of towns) {
         if (town.textContent.includes(searchedText.value.trim())) {
            selectedTowns.push(town);
            town.style.fontWeight = 'bold';
            town.style.textDecoration = 'underline';
         }
      }
   }
   

   result.textContent = selectedTowns.length + ' matches found';
}
