function solve() {
   const addButtons = Array.from(document.getElementsByClassName('add-product'));
   const checkoutButton = document.getElementsByClassName('checkout')[0];
   const basket = document.getElementsByTagName('textarea')[0];
   const allProducts = Array.from(document.getElementsByClassName('product-title'));
   allProducts.forEach((product) => {
      return product.textContent});
   for (const button of addButtons) {
      button.addEventListener('click', addClick);
   };

   checkoutButton.addEventListener('click', doCheckout);

   function addClick(e) {
      const addButton = e.currentTarget;
      const parent = addButton.parentNode.parentNode
      const productName = parent.getElementsByClassName('product-title')[0].textContent;
      const productPrice = parent.getElementsByClassName('product-line-price')[0].textContent;
      
      basket.textContent += `Added ${productName} for ${productPrice} to the cart.` + '\n'
   }

   function doCheckout(e) {
      const basket = document.getElementsByTagName('textarea')[0];
      let sum = 0;
      const productPattern = /(?<=Added )\w+/gm;
      const pricesPattern = /(?<= )[0-9\.]+/gm;
      const products = basket.textContent.match(productPattern);
      const prices = basket.textContent.match(pricesPattern);
      let uniqueProducts = [];
      if (products) {
         for (const product of products) {
            if (!uniqueProducts.includes(product)) {
               uniqueProducts.push(product);
            }
         }
      }
      
      if (prices) {
         for (const price of prices) {
            sum += Number(price);
         }
      }
      
      
      basket.textContent += `You bought ${uniqueProducts.join(', ')} for ${sum.toFixed(2)}.`
      for (const button of addButtons) {
         button.removeEventListener('click', addClick);
      }
      checkoutButton.removeEventListener('click', doCheckout);
   }
}