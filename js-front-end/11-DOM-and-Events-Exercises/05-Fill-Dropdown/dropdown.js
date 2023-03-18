function addItem() {
    const text = document.getElementById('newItemText');
    const value = document.getElementById('newItemValue');
    const selectContainer = document.getElementById('menu');
    const newOption = document.createElement('option');
    newOption.textContent = text.value;
    newOption.value = value.value;
    
    selectContainer.appendChild(newOption);
    text.value = '';
    value.value = '';
    
}