import os
from src.notion_client import NotionReader
from src.markdown_converter import MarkdownConverter
from src.mkdocs_generator import MkDocsGenerator

def main():
    notion_token = os.environ.get('NOTION_TOKEN')
    page_id = "106a350a0dad80d1aef6ddb540583c98"

    reader = NotionReader(notion_token)
    converter = MarkdownConverter()
    generator = MkDocsGenerator('docs')

    page_content = reader.get_page_content(page_id)
    block_children = reader.get_block_children(page_id)

    markdown_content = converter.convert_page_to_markdown(page_content, block_children)
    generator.save_markdown_file('index.md', markdown_content)
    generator.generate_mkdocs_config('My Notion Site')

    print("Markdown 文件已生成，MkDocs 配置已创建。")

if __name__ == "__main__":
    main()
