const execPython = require('./cmd.js').execPython
const fileDir = ['./raw/', './out/', './tmp/', './sort/']
const filename = '2.txt'

// console.log(fileArg);
// 调用 python 分析函数
// execPython(fileArg);

const divideText = (filename) => {
  let fileArg = fileDir.map((d) => d + filename).join(' ')
  execPython(fileArg);
}

const fs = require('fs')
const iGetInnerText = (txt) => {
    return txt.replace(/\ +/g, '').replace(/[]/g, '').replace(/[\r\n]/g, '')
}

fs.readFile('./raw/2.txt', (err, text) => {
    if (err) {
        throw err
    } else {
        // execPython(fileArg)
        console.log(text.toString());
        let data = iGetInnerText(text.toString());
        console.log(data);
        let filename = '3.txt';
        fs.writeFile('./raw/' + filename, data, (err) => {
          if (err) {
            throw err
          } else {
            console.log('Write '+ filename +'succes!')
            divideText(filename);
          }
        })
    }
})