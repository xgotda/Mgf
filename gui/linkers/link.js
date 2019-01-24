


function do_process(){
	console.log('starting');
	const {PythonShell} = require('python-shell')
	const path = require("path")

	var fileRead = document.getElementById('fileRead').value
	var fileWrite = document.getElementById('fileWrite').value
	var glycanppm = document.getElementById('glycanppm').value

	if (fileRead && fileWrite && glycanppm){
		var options = {
			scriptPath : path.join(__dirname, '../engine/'),
			args : [fileRead, fileWrite, glycanppm]
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
