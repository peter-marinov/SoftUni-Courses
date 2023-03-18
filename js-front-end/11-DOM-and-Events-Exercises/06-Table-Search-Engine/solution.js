function solve() {
   const searchedWord = document.getElementById('searchField');
   document.querySelector('#searchBtn').addEventListener('click', onClick);
   
   function onClick() {
      const rows = Array.from(document.querySelectorAll('.container tbody tr'));
      for (const row of rows) {
         let rowText = row.textContent.trim();
         if (rowText.includes(searchedWord.value.trim())) {
            // console.log(row.parentElement.nodeName)
            row.classList.add('select')
         } else {
            row.classList.remove('select')
         }
      }
      searchedWord.value = '';
   }
}