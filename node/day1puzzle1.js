const fetch = require('node-fetch');

const protectedUrl = "https://adventofcode.com/2019/day/1/input"
const cookie = 'session=/*ADD SESSION COOKIE HERE*/'
const arrSum = arr => arr.reduce((a,b) => a + b, 0)

const getInput = async () => {
    let response = await fetch(protectedUrl, {
        headers: {
            Cookie: cookie
        }
        });
    let data = await response.text();
    return data
}

getInput().then(data => {
    let inputs = data.split("\n")
    inputs = inputs.slice(0,inputs.length-1)
    
    for(let i = 0; i < inputs.length; i++){
      inputs[i] = parseInt(inputs[i])
      inputs[i] = Math.floor(inputs[i]/3) - 2
    }

    console.log(arrSum(inputs))
})