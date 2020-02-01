const express = require('express')
const app = express()

app.get('/', (req, res) => {

    const { spawn } = require('child_process');
    const pyProg = spawn('python', ['bot.py']);

    pyProg.stdout.on('data', function(data) {

        // console.log(data.toString());
        // res.write(data);
        res.end(
            '<html><body style = "display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center;"><h1><b>Please wait while the chatbot is opening.....</b></h1></body></html>');
    });
});

app.listen(3000, () => console.log('Application listening on port 3000'))