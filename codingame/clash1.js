const s = readline();
let cnt = 0
ans = '_'
hmap = new Object()
console.error(s)
for(i = 0; i < s.length; i++) {
    hmap[s[i]] = 0
}
for(i = 0; i < s.length; i++) {
    hmap[s[i]] +=1
}
for(i = 0; i < s.length; i++) {
    console.error(s[i])
    if(hmap[s[i]] == 1) {
        ans = s[i];
        break;
    }

}
console.log(ans);