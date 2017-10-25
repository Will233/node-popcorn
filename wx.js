const puppeteer = require('puppeteer')
const fs = require('fs')
const execPython = require('./cmd.js').execPython
// 暂停函数
const timeout = (time) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      try{
        resolve(1)
      } catch (e) {
        reject(0)
      }
    }, time)
  })
}

const url = 'http://www.jianshu.com/p/ec78f6489153'

puppeteer.launch().then(async browser => {
  let page = await browser.newPage()
  await page.goto(url)
  await timeout(2000)
  // 图文内容
  let article = await page.evaluate(() => {
    let body = document.getElementsByTagName('body')[0]
    return body.innerText
  })
  let idx = article.indexOf('\n')
  let title = article.slice(0,idx)
  console.log('### 标题 ###')
  console.log(title)
  let idx2 = article.indexOf('\n', idx + 1)
  let info = article.slice(idx, idx2)
  console.log('### 简介 ###')
  console.log(info)
  let content = article.slice(idx2)
  console.log('### 内容 ###')
  console.log(content)
  // 写入文件
  // const filename = title.concat('.txt')
  const filename = '1.txt'
  fs.writeFile('./raw/' + filename, content, (err) => {
    if (err) {
      throw err
    } else {
      execPython(filename)
      console.log('save success')
    }
  })

  browser.close()
})


