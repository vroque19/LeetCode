const fatherAge = parseInt(readline());
const N = parseInt(readline());

for (let i = 0; i < N; i++) {
    const childAge = parseInt(readline());
    child = childAge
    father = fatherAge

    while(father/child != 2) {
        child += 1
        father += 1
    }
    console.log(father)
}