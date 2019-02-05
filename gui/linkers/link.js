
processBtn = document.getElementById('process')
if(processBtn){
	processBtn.addEventListener('click', (event) => {
		// console.log('bob');
		var fileRead = document.getElementById('fileRead').value
		var fileWrite = document.getElementById('fileWrite').value
		var glycans = document.getElementById('glycans').value
		var glycanppm = document.getElementById('glycanppm').value
		var peptides = document.getElementById('peptides').value
		var peptideppm = document.getElementById('peptideppm').value
		var dblCharged = document.getElementById('dblCharged').checked
		var tplCharged = document.getElementById('tplCharged').checked
		// var spectraFile = document.getElementById('spectraFile').value
		// console.log('fileRead: ' + fileRead);


		console.log('glycans' + glycans);
		do_process()
	})
}

function do_process(){
	console.log('starting');
	const {PythonShell} = require('python-shell')
	const path = require("path")

	var fileRead = document.getElementById('fileRead').value
	var fileWrite = document.getElementById('fileWrite').value
	var glycans = document.getElementById('glycans').value
	var glycanppm = document.getElementById('glycanppm').value
	var peptides = document.getElementById('peptides').value
	var peptideppm = document.getElementById('peptideppm').value
	// var spectraFile = document.getElementById('spectraFile').value
	var dblCharged = document.getElementById('dblCharged').checked
	var tplCharged = document.getElementById('tplCharged').checked

// TODO: SET values of hardcoded glycans (box) to be names instead of numbers
// 	can then extract them and convert to actual values in code??

	if (fileRead && fileWrite && glycanppm){
		var options = {
			scriptPath : path.join(__dirname, '../../engine/'),
			args : [fileRead, fileWrite, glycans, glycanppm, peptides, peptideppm,
							dblCharged, tplCharged]
		}

		mgfprocess = new PythonShell('mgfMain.py', options)

		mgfprocess.on('message', function(message){
			console.log(message);
		})

		console.log('Finished processing .')
	} else{
		console.log('something was empty')
		console.log('fileRead: ' + fileRead +', fileWrite: ' + fileWrite
								+', glycan ppm: ' + glycanppm)
	}

}
