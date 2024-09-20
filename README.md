# Notion 到 MkDocs 转换器

这个项目是一个 Python 工具，用于将 Notion 页面转换为 Markdown 格式，并使用 MkDocs 生成静态网站。

## 功能特点

- 从 Notion API 读取页面内容
- 将 Notion 内容转换为 Markdown 格式
- 使用 MkDocs 生成静态网站
- 支持自动部署到 Vercel（需要额外配置）

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/your-username/notion-to-mkdocs.git
   cd notion-to-mkdocs
   ```

2. 创建并激活虚拟环境（可选但推荐）：
   ```
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 venv\Scripts\activate
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

## 配置

1. 在 Notion 中创建一个集成，并获取 API 密钥。

2. 设置环境变量：
   ```
   export NOTION_TOKEN=your_notion_api_key
   ```
   在 Windows 上，使用 `set` 而不是 `export`。

## 使用方法

1. 在 `main.py` 文件中设置您要转换的 Notion 页面 ID。

2. 运行主脚本：
   ```
   python main.py
   ```

3. 生成的 Markdown 文件将保存 `docs` 目录中，MkDocs 配置文件将生成为 `mkdocs.yml`。

4. 使用 MkDocs 构建网站：
   ```
   mkdocs build
   ```

5. 预览网站（可选）：
   ```
   mkdocs serve
   ```

## 部署到 Vercel

要将您的 Notion 到 MkDocs 项目部署到 Vercel，请按照以下步骤操作：

1. 确保您的项目已经推送到 GitHub 仓库。

2. 在项目根目录创建 `vercel.json` 文件，内容如下：

   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "mkdocs.yml",
         "use": "@vercel/static-build",
         "config": {
           "distDir": "site"
         }
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "/$1"
       }
     ]
   }
   ```

3. 在项目根目录创建 `.gitignore` 文件（如果还没有的话），并添加以下内容：

   ```
   venv/
   __pycache__/
   site/
   ```

4. 注册或登录 [Vercel](https://vercel.com/)。

5. 在 Vercel 仪表板中，点击 "New Project"。

6. 选择您的 GitHub 仓库，然后点击 "Import"。

7. 在配置页面：
   - 构建命令：`mkdocs build`
   - 输出目录：`site`
   - 安装命令：`pip install -r requirements.txt`

8. 展开 "Environment Variables" 部分，添加以下环境变量：
   - 名称：`NOTION_TOKEN`
   - 值：您的 Notion API 密钥

9. 点击 "Deploy" 开始部署过程。

10. 部署完成后，Vercel 将提供一个 URL，您可以通过该 URL 访问您的网站。

11. （可选）如果您想要在每次推送到 GitHub 时自动更新网站，可以在本地运行以下命令：

    ```bash
    pip install vercel
    vercel login
    ```

    然后，每次您想更新网站时，只需运行：

    ```bash
    vercel --prod --yes
    ```

注意：确保您的 `requirements.txt` 文件包含所有必要的依赖，包括 `mkdocs` 和 `mkdocs-material`。

通过这种设置，每次您推送更改到 GitHub 仓库时，Vercel 将自动重新构建和部署您的网站。这样，您的 Notion 内容更改将自动反映在您的网站上。

## 贡献

欢迎贡献！请随时提交 pull requests 或开 issues 来改进这个项目。

## 许可证

[MIT License](LICENSE)