const fetch = require('node-fetch');

const protectedUrl = "https://adventofcode.com/2019/day/1/input"
const cookie = 'session=53616c7465645f5ff85d2293bbb71faf9caeca66488104faf5a9521d283e71820d260467637fc8429493184cdd9a020c'
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