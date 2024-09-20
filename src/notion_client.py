from notion_client import Client

class NotionReader:
    def __init__(self, token):
        self.client = Client(auth=token)

    def get_page_content(self, page_id):
        return self.client.pages.retrieve(page_id=page_id)

    def get_block_children(self, block_id):
        return self.client.blocks.children.list(block_id=block_id)