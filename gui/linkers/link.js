function do_process(){
	const {PythonShell} = require('python-shell')
	const path = require("path")


	var fileRead = document.getElementById('fileRead').files[0].path
	//document.getElementById('fileRead').value = ''
	var fileWrite = document.getElementById('fileWrite').value
	//document.getElementById('fileWrite').value = ''
	var aTolerance = document.getElementById('aTolerance').value
	document.getElementById('aTolerance').value = '0.02'

	var options = {
		scriptPath : path.join(__dirname, '../engine/'),
		args : [fileRead, fileWrite, aTolerance]
	}

	let mgfprocess = new PythonShell('fileio.py', options)

	// mgfprocess.end(function(err, code, message){
	// 	swal("Done!", err + '\n' + options.args + '\n '+ code + '\n\n ' + message)
	// })

	mgfprocess.on('message', function(message){
		swal(message)
	})
}
