# py-api-practice

本项目用于练习 Python 调用 API、环境变量管理、配置分离、以及使用 PyGithub 访问 GitHub API。  
项目结构清晰，适合作为后续 API 学习与工程化实践的基础模板。

---

## 📁 项目结构（Project Structure）

```
py-api-practice/
│── main.py               # 昨天完成：使用 PyGithub 获取仓库列表
│── APIRequest.py         # 预留：后续封装通用 API 请求类
│── config.py             # 负责加载 .env 环境变量
│── characters.json       # 示例数据文件
│── requirements.txt      # Python 依赖
│── .env                  # 环境变量（不要上传）
│── .venv/                # 虚拟环境
│── pycache/          # Python 缓存文件
```

---

## ⚙️ 环境安装（Environment Setup）

### 1. 克隆项目
```
git clone https://github.com/你的用户名/py-api-practice.git (github.com in Bing)
cd py-api-practice
```

### 2. 创建虚拟环境（可选）
```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.\.venv\Scripts\activate    # Windows
```

### 4. 配置 `.env`
```
GITHUB_TOKEN=你的token
GITHUB_HOSTNAME=https://api.github.com
```

---

## 🚀 运行项目
```
python main.py
```

---

## 🗂️ 版本历史（Changelog）

本项目会随着每日练习不断更新，以下记录每次提交的主要内容，便于追踪学习进度与功能演进。

---

### v0.1.0 — 2026-04-20
**内容：完成 GitHub API 基础调用**
- 新增 `main.py`：使用 PyGithub 获取当前用户的仓库列表  
- 新增 `config.py`：加载 `.env` 环境变量  
- 新增 `.env` 示例（未上传）  
- 初始化项目结构  
- 完成首次 API 调用测试  

### v0.2.0 — 2026-04-21
**内容：新增 Rick and Morty API 全量数据抓取功能**
- 新增 `get_base_url()`：支持分页请求  
- 新增 `get_all_characters()`：循环抓取所有页面数据  
- 新增 `get_character_data()`：按页抓取角色数据  
- 新增 `save_to_json()`：将抓取结果保存为 `characters.json`  
- 新增 `characters.json` 数据文件  
- 新增 Pandas DataFrame 预览（`df.head()`）  
- 完成 API 数据清洗与结构化处理  
- 项目结构进一步完善  

---




## 📚 学习目标

- 熟悉 Python 环境变量管理（dotenv）
- 掌握 PyGithub 的基本使用方法
- 理解 API 调用的工程化结构
- 为后续 API 项目打基础






