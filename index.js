const express = require('express');
const app = express();

app.get('/run', function(req, res){
  eval(req.query.code); // ⚠️ Unsafe for demo
});

app.listen(3000, () => console.log('Demo app running on port 3000'));