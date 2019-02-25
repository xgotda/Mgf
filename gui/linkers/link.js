const {PythonShell} = require('python-shell')
const path = require("path")
const {ipcRenderer} = require('electron');

const PY_FOLDER = './../engine/'


processBtn = document.getElementById('process')
if(processBtn){
	processBtn.addEventListener('click', (event) => {
		// console.log('bob');
		// var fileRead = document.getElementById('fileRead').value
		// var fileWrite = document.getElementById('fileWrite').value
		// var glycans = document.getElementById('glycans').value
		// var glycanppm = document.getElementById('glycanppm').value
		// var peptides = document.getElementById('peptides').value
		// var peptideppm = document.getElementById('peptideppm').value
		// var dblCharged = document.getElementById('dblCharged').checked
		// var tplCharged = document.getElementById('tplCharged').checked

		// console.log('glycans' + glycans);
		do_process()
	})
}

function do_process(){
	console.log('starting');

	var fileRead = document.getElementById('fileRead').value
	var fileWrite = document.getElementById('fileWrite').value
	var glycans = document.getElementById('glycans').value
	var glycanppm = document.getElementById('glycanppm').value
	var peptides = document.getElementById('peptides').value
	var peptideppm = document.getElementById('peptideppm').value
	var dblCharged = document.getElementById('dblCharged').checked
	var tplCharged = document.getElementById('tplCharged').checked

// TODO: SET values of hardcoded glycans (box) to be names instead of numbers
// 	can then extract them and convert to actual values in code??


	if (fileRead && fileWrite && glycanppm){
		var options = {
			scriptPath : path.join(__dirname, PY_FOLDER),
			args : [fileRead, fileWrite, glycans, glycanppm, peptides, peptideppm,
							dblCharged, tplCharged]
		}

		mgfprocess = new PythonShell('mgfMain.py', options)

		// PythonShell.run('my_script.py', options, function (err, results) {
		//   if (err) throw err;
		//   // results is an array consisting of messages collected during execution
		//   console.log('results: %j', results);
		// });
		// ```

		// document.getElementById('feedfs').hidden = "false"
		document.getElementById('feedback').innerHTML = "Started processing..."

		mgfprocess.on('error', function(error) {
			ipcRenderer.send('process:show', 'Error: ' + error)
			console.log(error);
		})

		mgfprocess.on('message', function(message){
			ipcRenderer.send('process:show', message)
			console.log(message);
		})

		mgfprocess.end(function(err, code, signal) {
			if (err) throw err;
			console.log('code: ' + code +'. signal: ' + signal);
			document.getElementById('feedback').innerHTML = "Finished processing."
			console.log('Finished processing .')
		})
	} else{
		ipcRenderer.send('process:show', 'Incomplete information')
		console.log('something was empty')
		console.log('fileRead: ' + fileRead +', fileWrite: ' + fileWrite
								+', glycan ppm: ' + glycanppm)
	}

}
