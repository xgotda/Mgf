
// // This file is required by the index.html file and will
// // be executed in the renderer process for that window.
// // All of the Node.js APIs are available in this process.
//


const {dialog} = require('electron').remote
const {ipcRenderer} = require('electron');

const fileManagerBtn = document.getElementById('ofm')
if(fileManagerBtn){
  fileManagerBtn.addEventListener('click', (event) => {
    ipcRenderer.send('ofmRequest')
  })
}

ipcRenderer.on('ofmRequest', function(e, selected){
  document.getElementById('fileRead'). value = selected
})
