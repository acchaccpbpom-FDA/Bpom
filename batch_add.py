 # --- 这里是你要改的地方 ---
# 1. 把你要插入的代码复制到下面的引号里
code_to_add = '''
<link rel="icon" href="FDA商标.png" type="image/png">
'''
# 2. 要插入到哪个标签后面？这里默认是 <head>
target_tag = '<head>'

# --- 下面的不用改 ---
import os

# 自动找当前文件夹里所有的 .html 文件
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            print(f"正在处理: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 在目标标签后插入代码
            new_content = content.replace(target_tag, f'{target_tag}{code_to_add}')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
print("✅ 所有文件处理完成！")