import os
import yaml

class MkDocsGenerator:
    def __init__(self, docs_dir):
        self.docs_dir = docs_dir

    def save_markdown_file(self, filename, content):
        filepath = os.path.join(self.docs_dir, filename)
        # 确保目录存在
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def generate_mkdocs_config(self, site_name):
        config = {
            'site_name': site_name,
            'theme': 'material',
            'nav': [
                {'Home': 'index.md'},
                # 可以根据生成的文档动态添加导航
            ]
        }
        with open('mkdocs.yml', 'w') as f:
            yaml.dump(config, f)
