import os

忽略目录 = ['.git', '.vscode', '__pycache__', '.github']
忽略文件 = ['index.html', 'build.py', '.gitignore', 'README.md']

网页头部 = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>学习档案库</title>
<style>
body { font-family: sans-serif; padding: 15px; background: #f4f7f6; max-width: 800px; margin: 0 auto;}
.card { background: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; display: block; text-decoration: none; color: #333; box-shadow: 0 2px 5px rgba(0,0,0,0.05);}
.card:active { background: #eee; transform: scale(0.98); }
.title { color: #3498db; font-weight: bold; font-size: 16px; margin-bottom: 4px;}
.category { font-size: 18px; color: #7f8c8d; margin: 25px 0 12px 0; border-left: 4px solid #3498db; padding-left: 10px;}
</style>
</head>
<body>
<h2>学习档案库</h2>
"""

网页尾部 = """
</body>
</html>
"""

网页主体 = ""
所有项目 = os.listdir('.')

for 文件夹名 in 所有项目:
    if os.path.isdir(文件夹名) and 文件夹名 not in 忽略目录:
        网页主体 += f'<div class="category">{文件夹名}</div>\n'
        目录内容 = os.listdir(文件夹名)
        for 文件名 in 目录内容:
            if 文件名 not in 忽略文件:
                文件路径 = f"{文件夹名}/{文件名}"
                网页主体 += f'<a href="{文件路径}" class="card"><div class="title">{文件名}</div></a>\n'

with open('index.html', 'w', encoding='utf-8') as 文件对象:
    文件对象.write(网页头部 + 网页主体 + 网页尾部)