import os

忽略目录 = ['.git', '.vscode', '__pycache__', '.github']
忽略文件 = ['index.html', 'build.py', '.gitignore', 'README.md']

网页头部 = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>uiggiii's repository</title>
<style>
:root { --primary: #3498db; --bg: #f8f9fa; --text: #2c3e50; }
body { font-family: -apple-system, system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 20px; max-width: 800px; margin: 0 auto; }
h1 { text-align: center; color: var(--primary); font-size: 28px; margin-bottom: 30px; }

/* 搜索框样式 */
.search-container { position: sticky; top: 10px; z-index: 100; margin-bottom: 25px; }
#searchInput { width: 100%; padding: 15px; border: 2px solid #ddd; border-radius: 12px; font-size: 16px; box-sizing: border-box; outline: none; transition: border-color 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
#searchInput:focus { border-color: var(--primary); }

/* 折叠组样式 */
details { background: white; margin-bottom: 15px; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
summary { padding: 15px; font-weight: bold; cursor: pointer; background: white; list-style: none; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #f0f0f0; }
summary::-webkit-details-marker { display: none; }
summary::after { content: '▶'; font-size: 12px; transition: transform 0.3s; color: #ccc; }
details[open] summary::after { transform: rotate(90deg); }

/* 卡片链接样式 */
.file-list { padding: 10px; }
.card { display: block; padding: 12px 15px; margin: 5px 0; background: #fff; text-decoration: none; color: #444; border-radius: 6px; border-left: 3px solid transparent; transition: all 0.2s; font-size: 14px; }
.card:hover { background: #f0f7ff; border-left-color: var(--primary); padding-left: 20px; }
</style>
</head>
<body>
<h1>uiggiii's repository</h1>

<div class="search-container">
    <input type="text" id="searchInput" placeholder="搜索文件名..." onkeyup="filterFiles()">
</div>

<div id="repo-content">
"""

网页尾部 = """
</div>

<script>
function filterFiles() {
    let input = document.getElementById('searchInput').value.toLowerCase();
    let cards = document.getElementsByClassName('card');
    let groups = document.getElementsByTagName('details');

    for (let card of cards) {
        let fileName = card.innerText.toLowerCase();
        if (fileName.includes(input)) {
            card.style.display = "";
        } else {
            card.style.display = "none";
        }
    }

    // 如果组内有匹配的文件，自动展开该组；如果没有匹配，则隐藏该组
    for (let group of groups) {
        let visibleCards = group.querySelectorAll('.card[style="display: "], .card:not([style])');
        if (visibleCards.length > 0) {
            group.style.display = "";
            if (input !== "") group.open = true;
        } else {
            group.style.display = "none";
        }
    }
}
</script>
</body>
</html>
"""

网页主体 = ""
所有项目 = sorted(os.listdir('.'))

for 文件夹名 in 所有项目:
    if os.path.isdir(文件夹名) and 文件夹名 not in 忽略目录:
        网页主体 += f'<details open>\n<summary>{文件夹名}</summary>\n<div class="file-list">\n'
        目录内容 = sorted(os.listdir(文件夹名))
        for 文件名 in 目录内容:
            if 文件名 not in 忽略文件:
                文件路径 = f"{文件夹名}/{文件名}"
                网页主体 += f'<a href="{文件路径}" class="card">{文件名}</a>\n'
        网页主体 += '</div>\n</details>\n'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(网页头部 + 网页主体 + 网页尾部)
