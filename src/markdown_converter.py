class MarkdownConverter:
    def convert_page_to_markdown(self, page_content, block_children):
        # 实现将 Notion 页面内容转换为 Markdown 的逻辑
        markdown_content = "# " + page_content['properties']['title']['title'][0]['plain_text'] + "\n\n"
        for block in block_children['results']:
            markdown_content += self.convert_block_to_markdown(block)
        return markdown_content

    def convert_block_to_markdown(self, block):
        # 检查 'paragraph' 和 'rich_text' 是否存在且不为空
        if 'paragraph' in block and 'rich_text' in block['paragraph'] and block['paragraph']['rich_text']:
            return block['paragraph']['rich_text'][0]['plain_text'] + "\n\n"
        else:
            return ""  # 或者返回一个默认值