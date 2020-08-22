const express = require('express')
const app = express()
const port = 5000

app.get('/', (req, res) => res.send({ response: 'Hello, orders!' }))

app.listen(port)
