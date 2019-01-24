

const {ipcRenderer} = require('electron');

// Send value to main when clicked 'Enter'
const glycanForm = document.getElementById('glycanForm')
glycanForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const glycan = document.querySelector('#glycan').value;
  ipcRenderer.send('glycan:add', glycan);
})
