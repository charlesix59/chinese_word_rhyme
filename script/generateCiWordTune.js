import Cilin from "../data/Cilin_Rhyme.json" assert {type:"json"}
import * as fs from "node:fs/promises"

const map = new Map()
let flag = false;

for(let rPart in Cilin){
  if(rPart == "第十五部"){
    flag = true
  }
  if(flag){
    for(let word of Cilin[rPart]["入声"]){
      if(map.has(word)){
        const temp = map.get(word);
        if(temp.tune == "平"){
          temp.tune = "多";
        }
        if(temp.rhyme != rPart){
          temp.rhyme = "多";
        }
        map.set(word,temp);
        continue;
      }
      map.set(word,{tune: "仄",rhyme: rPart})
    }
    continue;
  }
  for(let word of Cilin[rPart]["平声"]){
    if(map.has(word)){
      const temp = map.get(word);
      if(temp.tune == "仄"){
        temp.tune = "多";
      }
      if(temp.rhyme != rPart){
        temp.rhyme = "多";
      }
      map.set(word,temp);
      continue;
    }
    map.set(word,{tune: "平",rhyme: rPart})
  }
  for(let word of Cilin[rPart]["仄声"]){
    if(map.has(word)){
      const temp = map.get(word);
      if(temp.tune == "平"){
        temp.tune = "多";
      }
      if(temp.rhyme != rPart){
        temp.rhyme = "多";
      }
      map.set(word,temp);
      continue;
    }
    map.set(word,{tune: "仄",rhyme: rPart})
  }
}

console.log(JSON.stringify(Object.fromEntries(map)))

fs.writeFile("../data/Ci_Word_Tune.json", JSON.stringify(Object.fromEntries(map)), "utf-8");