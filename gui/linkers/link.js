

processBtn = document.getElementById('process')
if(processBtn){
	processBtn.addEventListener('click', (event) => {
		do_process()
	})
}

function do_process(){
	const {PythonShell} = require('python-shell')
	const path = require("path")

	var fileRead = document.getElementById('fileRead').value
	var fileWrite = document.getElementById('fileWrite').value
	var aTolerance = document.getElementById('aTolerance').value

	var options = {
		scriptPath : path.join(__dirname, '../engine/'),
		args : [fileRead, fileWrite, aTolerance]
	}

	let mgfprocess = new PythonShell('mgfMain.py', options)

	mgfprocess.on('message', function(message){
		console.log(message);
	})
	document.getElementById('fileWrite').value = "fffff"
	console.log('Finished processing .')

	// mgfprocess.end(function(err, code, message){
		//
		// 	swal("Done!", str(err) + '\n' + str(options.args) + '\n '+ str(code) + '\n\n ' + str(message))
		// 	document.getElementById('aTolerance').value = 3
		// 	document.getElementById('fileWrite').value = fileWrite
		// 	document.getElementById('fileRead').value = fileRead
		// })
}
