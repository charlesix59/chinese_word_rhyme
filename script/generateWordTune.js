import pingshui from "../data/Pingshui_Rhyme.json" assert {type:"json"}
import * as fs from "node:fs/promises"

const map = new Map();
for(const part in pingshui["上平声部"]){
    for(const char of pingshui["上平声部"][part]){
        if(!map.has(char)){
            map.set(char,"平");
        }
    }
}
for(const part in pingshui["下平声部"]){
    for(const char of pingshui["下平声部"][part]){
        if(!map.has(char)){
            map.set(char,"平");
        }
    }
}
for(const part in pingshui["上声部"]){
    if(!(pingshui["上声部"][part] instanceof Array)){
        break;
    }
    for(const char of pingshui["上声部"][part]){
        if(map.has(char) && map.get(char)==="平"){
            map.set(char,"多");
        }
        else{
            map.set(char,"仄");
        }
    }
}
for(const part in pingshui["去声部"]){
    for(const char of pingshui["去声部"][part]){
        if(map.has(char) && map.get(char)==="平"){
            map.set(char,"多");
        }
        else{
            map.set(char,"仄");
        }
    }
}
for(const part in pingshui["入声部"]){
    for(const char of pingshui["入声部"][part]){
        if(map.has(char) && map.get(char)==="平"){
            map.set(char,"多");
        }
        else{
            map.set(char,"仄");
        }
    }
}
console.log(JSON.stringify(Object.fromEntries(map)))

fs.writeFile("../data/Word_Tune.json", JSON.stringify(Object.fromEntries(map)), "utf-8");

