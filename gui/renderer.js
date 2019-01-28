
// // This file is required by the index.html file and will
// // be executed in the renderer process for that window.
// // All of the Node.js APIs are available in this process.
//

const {dialog} = require('electron').remote
const {ipcRenderer} = require('electron');

// From AddGlycans
const glycansText = document.getElementById('glycans')
ipcRenderer.on('staticGlycan:add', function(e, glycan){
  removeDuplicates(glycansText, glycan)
});


// Open file manager for mgf file.
const fileManagerBtn = document.getElementById('ofm')
if(fileManagerBtn){
  fileManagerBtn.addEventListener('click', (event) => {
    ipcRenderer.send('ofmRequest')
  })
}
ipcRenderer.on('ofmRequest', function(e, selected){
  document.getElementById('fileRead').value = selected
})

// Open file manager for spectra file.
const spectraFileBtn = document.getElementById('spectra')
if(spectraFileBtn){
  spectraFileBtn.addEventListener('click', (event) => {
    ipcRenderer.send('spectraRequest')
  })
}
ipcRenderer.on('spectraRequest', function(e, selected){
  document.getElementById('spectraFile').value = selected
})


// Save file manager
const fileWriteBtn = document.getElementById('sfm')
if(fileWriteBtn){
  fileWriteBtn.addEventListener('click', (event) => {
    ipcRenderer.send('sfRequest')
  })
}
ipcRenderer.on('sfRequest', function(e, selected){
  document.getElementById('fileWrite'). value = selected
})


processBtn = document.getElementById('process')
if(processBtn){
	processBtn.addEventListener('click', (event) => {
		do_process()
	})
}

glycansText.addEventListener('mousemove', (e) => {
  removeDuplicates(glycansText, '')
})
const peptidesText = document.getElementById('peptides')
peptidesText.addEventListener('mousemove', (e) => {
  removeDuplicates(peptidesText, '')
})


// Remove duplicate values in textbox. (Pass in box and values to add.)
function removeDuplicates(valTextWin, newVals){
  oldArr = valTextWin.value.split('\n')
  allVals = oldArr.concat(newVals)

  // TODO: Does not remove newline if in the middle!! FIX!
  uniqueVals = Array.from(new Set(allVals));
  // console.log(uniqueVals.toString());
  valTextWin.value = ''
  uniqueVals.forEach((item, index) => {
    valTextWin.value = valTextWin.value + item + '\n'
  })
}
