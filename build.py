import os

# 过滤掉不需要显示的系统文件夹和工具文件
忽略目录 = ['.git', '.vscode', '__pycache__', '.github']
忽略文件 = ['index.html', 'build.py', '.gitignore', 'README.md']

网页头部 = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>uiggiii's repository</title>
<style>
:root { --primary: #3498db; --bg: #f8f9fa; --text: #2c3e50; --card: #ffffff; }
body { font-family: -apple-system, system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 20px; max-width: 800px; margin: 0 auto; line-height: 1.6; }
h1 { text-align: center; color: var(--primary); margin-bottom: 30px; font-weight: 800; }

/* 搜索框 */
.search-container { position: sticky; top: 10px; z-index: 100; margin-bottom: 25px; }
#searchInput { width: 100%; padding: 15px; border: 2px solid #ddd; border-radius: 12px; font-size: 16px; box-sizing: border-box; outline: none; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: 0.3s; }
#searchInput:focus { border-color: var(--primary); }

/* 折叠容器 */
details { background: var(--card); margin-bottom: 15px; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.05); border: 1px solid #eee; }
summary { padding: 16px; font-weight: bold; cursor: pointer; display: flex; justify-content: space-between; align-items: center; user-select: none; }
summary::-webkit-details-marker { display: none; }
summary::after { content: '▶'; font-size: 10px; color: #bbb; transition: 0.3s; }
details[open] summary::after { transform: rotate(90deg); }
details[open] summary { border-bottom: 1px solid #f5f5f5; }

/* 文件列表与卡片 */
.file-list { padding: 10px; }
.card-item { display: flex; justify-content: space-between; align-items: center; padding: 12px; margin: 6px 0; background: #fff; border-radius: 8px; border: 1px solid #f0f0f0; transition: 0.2s; }
.card-item:hover { background: #f9fcff; border-color: var(--primary); transform: translateX(5px); }
.file-info { text-decoration: none; color: #444; font-size: 14px; flex-grow: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; margin-right: 10px; }
.preview-btn { padding: 5px 12px; font-size: 12px; color: var(--primary); border: 1px solid var(--primary); border-radius: 6px; text-decoration: none; transition: 0.2s; }
.preview-btn:hover { background: var(--primary); color: #fff; }
</style>
</head>
<body>
<h1>uiggiii's repository</h1>
<div class="search-container"><input type="text" id="searchInput" placeholder="输入关键字搜索文件..." onkeyup="filterFiles()"></div>
<div id="repo-content">
"""

网页尾部 = """
</div>
<script>
function filterFiles() {
    let input = document.getElementById('searchInput').value.toLowerCase();
    let cards = document.getElementsByClassName('card-item');
    let groups = document.getElementsByTagName('details');

    if (input !== "") {
        for (let g of groups) g.open = true;
    }

    for (let card of cards) {
        let text = card.querySelector('.file-info').innerText.toLowerCase();
        card.style.display = text.includes(input) ? "" : "none";
    }

    for (let group of groups) {
        let hasVisible = group.querySelectorAll('.card-item[style="display: "], .card-item:not([style])').length > 0;
        group.style.display = hasVisible ? "" : "none";
    }
}
</script>
</body>
</html>
"""

网页主体 = ""
# 获取所有文件夹并按字母排序
所有项目 = sorted([d for d in os.listdir('.') if os.path.isdir(d) and d not in 忽略目录])

for 文件夹名 in 所有项目:
    网页主体 += f'<details open>\n<summary>{文件夹名}</summary>\n<div class="file-list">\n'
    目录内容 = sorted(os.listdir(文件夹名))
    for 文件名 in 目录内容:
        if 文件名 not in 忽略文件:
            路径 = f"{文件夹名}/{文件名}"
            ext = 文件名.split('.')[-1].lower()
            # 预览链接逻辑
            if ext in ['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx']:
                预览链接 = f"https://docs.google.com/viewer?url=https://uiggiii.github.io/{路径}&embedded=true"
            else:
                预览链接 = 路径
            
            网页主体 += f'''
            <div class="card-item">
                <a href="{路径}" class="file-info" download>{文件名}</a>
                <a href="{预览链接}" target="_blank" class="preview-btn">预览</a>
            </div>'''
    网页主体 += '</div>\n</details>\n'

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(网页头部 + 网页主体 + 网页尾部)
