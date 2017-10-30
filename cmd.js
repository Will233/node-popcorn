// node.js 调用系统命令

const exec = require('child_process').exec
const execPython = (python, args) => {
  exec('python '+ python + ' ' + args , (error, stdout, stderr) => {
    if (stdout.length > 1) {
      console.log('you offer args:', stdout);
      console.log('\n');
    } else {
      console.log('you don\'t offer args');
    }
    if (error) {
      console.info('stderr : ' + stderr);
    }
  })
}

/**
 * 语义分词
 * option = {
 *      source: './raw/source-demo.txt',
 *      target: './out/target-demo.txt',
 *      engine: 'jieba',
 *      dictionary: ''// 字典
 *   } 
 */
const segment = (opt) => {
  console.log(opt)
  const dictionary = opt.dictionary
  const engine = opt.engine 
  const source = opt.source 
  const target = opt.target
  const args = [source, target, engine, dictionary].join(' ')
  execPython('./python/segment.py', args)
}

/**
 * 简单的分析
 * option = {
 *      source: './raw/source-demo.txt',
 *      target: './out/target-demo.txt'
 *   } 
 */
const analysis = (opt) => {
  // console.log(opt)
  const source = opt.source 
  const target = opt.target
  const args = [source, target].join(' ')
  execPython('./python/analysis.py', args)
}

module.exports ={
  execPython: execPython,
  segment: segment,
  analysis: analysis
}
