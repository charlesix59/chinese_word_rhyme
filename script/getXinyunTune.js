import * as fs from "node:fs/promises";

const tunes = ["阴平", "阳平", "上声", "去声"];
const chineseNumbers = [
  "一",
  "二",
  "三",
  "四",
  "五",
  "六",
  "七",
  "八",
  "九",
  "十",
  "十一",
  "十二",
  "十三",
  "十四",
];

const isTuneName = (str) => {
  for (let tune of tunes) {
    if (str.includes(tune)) {
      return tune;
    }
  }
  return false;
};

function removeParentheses(str) {
  return str.replace(/（[^)]*?）/g, ""); // 使用正则表达式匹配括号及其内部的内容，并替换为空字符串
}

fs.readFile("./script/data/xinyun.txt", { encoding: "utf8" }).then((data) => {
  const dir = {};
  let word = {};
  let key = "";
  let tuneItem = "";
  const splitData = data
    .split("\n")
    .map((str) => str.trim())
    .filter((str) => str);
  for (let sentense of splitData) {
    if (chineseNumbers.includes(sentense[0])) {
      dir[key] = word;
      key = sentense.split("　")[0];
      word = {};
      continue;
    }
    const str = removeParentheses(sentense);
    if (isTuneName(str)) {
      tuneItem = isTuneName(str);
      if (tuneItem === "阴平" || tuneItem === "阳平") {
        tuneItem = "平";
      } else {
        tuneItem = "仄";
      }
      continue;
    }
    word[tuneItem] = word[tuneItem] || [];
    word[tuneItem].push(...str.split(""));
  }
  fs.writeFile("./data/Xinyun_Rhyme.json", JSON.stringify(dir));
});
