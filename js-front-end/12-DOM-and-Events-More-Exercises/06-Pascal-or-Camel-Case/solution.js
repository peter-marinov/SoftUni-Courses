function solve() {
  const text = document.getElementById('text');
  const namingConviction  = document.getElementById('naming-convention');
  const result = document.getElementById('result');

  let words = text
    .value
    .split(' ')
    .map((w) => {
      return w.toLowerCase()
    });
  
  if (namingConviction.value === "Camel Case") {
    for (let i = 0; i < words.length; i++) {
      let currentWord = words[i];
      if (i === 0) {
        result.textContent += words[i];
      } else {
        result.textContent += currentWord[0].toUpperCase() + currentWord.slice(1);
      }
    }
  } else if (namingConviction.value === "Pascal Case") {
    for (let i = 0; i < words.length; i++) {
      let currentWord = words[i];
      result.textContent += currentWord[0].toUpperCase() + currentWord.slice(1);
    }
  } else {
    result.textContent = 'Error!';
  }
}