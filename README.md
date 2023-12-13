# chinese_word_rhyme
一个汉字字典释义、汉字平仄、平水韵与词林正韵的json格式数据存储仓库，用于诗词格律查询与古文释义查询。

仓库维护中，如果你觉得这个仓库对你有用处，并且你也对此感兴趣，请帮我一起维护仓库。

## 文件与结构

### 平水韵

所在文件：`Pingshui_Rhyme.json`

数据结构：

```json
{
    "上平声部": { // 声部
        "一东": [ // 韵部
            "东", // 包含文字
            "......"
        ],
    }
}
```

### 古文解释

所在文件：`Word_Explain.json`

数据结构：

```json
{
    "阿": [ // key为文字，value为一或多个发音数组
        {
            "pronunciation": "ā", // 发音
            "explains": [ // 在该发音下存在的释义
                "词头，多用在亲属名称或人名的前面，盛行于魏晋以后。《孔雀东南飞》：“～母谓～女：‘适得府君书，明日来迎汝。’”《颜氏家训·风操》：“梁武小名～练，子孙呼练为绢。”"
            ]
        }
    ],
}
```

## 参考资料与信息源

### 平水韵

[平水韵 - 维基文库，自由的图书馆 (wikisource.org)](https://zh.wikisource.org/zh-hans/%E5%B9%B3%E6%B0%B4%E9%9F%BB)

### 古文释义

[使用者:Wihwang/古漢語常用字字典 - 維基詞典，自由的多語言詞典 (wiktionary.org)](https://zh.wiktionary.org/zh-hant/User:Wihwang/%E5%8F%A4%E6%BC%A2%E8%AA%9E%E5%B8%B8%E7%94%A8%E5%AD%97%E5%AD%97%E5%85%B8)

[ksanaforge/guhanyu: 古漢語常用字典 (github.com)](https://github.com/ksanaforge/guhanyu)

[pwxcoo/chinese-xinhua: :orange_book: 中华新华字典数据库。包括歇后语，成语，词语，汉字。 (github.com)](https://github.com/pwxcoo/chinese-xinhua)