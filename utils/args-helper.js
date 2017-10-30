/** 
 * 获取命令行参数的工具
 */

/**
 * @see 根据选项名获取选项的值
 * @param {String} sname :short name of option
 * @param {String} lname : long name of option   
 */
const getOption = (sname, lname) => {
  const _arr = process.argv
  let lpos = _arr.indexOf(lname)
  if (lpos > -1) {
    return _arr[lpos + 1]
  } else {
    let spos = _arr.indexOf(sname)
    return spos > -1 ? _arr[spos + 1] : ''
  }
}

/**
 * @see 获取一个包含所有选项的对象
 * @param {Object} program ,commander.js 提供的program对象
 * @return { optionName: optionValue ...}
 */
const getAllOption = (program) => {
  let option = {}
  if (program == null || program == undefined) {
    return option
  }
  let _opts = program.options
   _opts.map( op => {
    let nameItem = op.long ? op.long : op.short
    option[nameItem.replace(/^-+/, '')] = getOption(op.short, op.long)
    return op
  })
  return option
}
module.exports = {
  getAllOption
}