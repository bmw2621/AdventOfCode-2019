var possibilities = []
var cleaned = []

for(let i = 402328; i <= 864247; i++){
    possibilities.push(i)
}
var nums = ['00','11','22','33','44','55','66','77','88','99']
for(let i = 0; i < possibilities.length; i++){
    let containsTest = false
    let possibility = possibilities[i]
    nums.forEach( testValue =>{
        if(possibility.toString().includes(testValue)){
            containsTest = true
        }
    })

    let split_possibility = []
    for(let i = 0; i < possibility.toString().length; i++){
        split_possibility.push(parseInt(possibility.toString().charAt(i)))
    }

    let gtet_test = true
    for(let i = 0; i < 5; i++){
        if(split_possibility[i] > split_possibility[i + 1]){
            gtet_test = false
        }
    }

    if(containsTest && gtet_test){
        cleaned.push(possibility)
    }
}

console.log(cleaned)
console.log(cleaned.length)

