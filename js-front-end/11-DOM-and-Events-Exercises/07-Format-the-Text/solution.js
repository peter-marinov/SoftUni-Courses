function solve() {
  output = document.getElementById('output');
  const textarea = document.getElementById('input');
  let sentences = textarea.value.split('.');
  sentences.pop();


  while (sentences.length > 0) {
    let paragraphSentences = sentences.splice(0, 3)
      .map((p) => p.trimStart());
    const newParagraph = document.createElement('p');
    newParagraph.textContent = paragraphSentences.join('.') + '.';
    output.appendChild(newParagraph);
  }
 

}

 // const input = document.getElementById('input');
  // const output = document.getElementById('output');
  // const sentencePattern = /\(?[^\.\?\!]+[\.!\?]\)?/g;
  // const sentences = input.value.match(sentencePattern);
  // for (let i = 0; i < sentences.length; i+=3) {
  //   let newParagraph = document.createElement('p')
  //   let newSentence = sentences[i];
  //   if (i + 1 < sentences.length) {
  //     newSentence += sentences[i + 1] + ' ';
  //   }
  //   if (i + 2 < sentences.length) {
  //     newSentence += sentences[i + 2] + ' ';
  //   }
  //   newParagraph.textContent = newSentence;

  //   output.appendChild(newParagraph);
  // }