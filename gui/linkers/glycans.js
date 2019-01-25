

const {ipcRenderer} = require('electron');

// Send value to main when clicked 'Enter'
const glycanForm = document.getElementById('glycanForm')
glycanForm.addEventListener('submit', (e) => {
  e.preventDefault()
  var glycan = []
  for(var i = 0; i < glycanForm.elements.length-1; i++){
    val = glycanForm[i]
    if ((val.type == "checkbox") && (val.checked)){
      glycan.push(val.value)
    }
  }
  ipcRenderer.send('glycan:add', glycan)
})
