# 复分析：可视化方法 · 知枢学习系统

Needham《复分析：可视化方法》的点化学习库：章节精讲、概念页、深度推导、测验、抽认卡、术语表，统一收在 `index.html` 一个入口里。

## 本地怎么用

双击打开 `index.html`。顶部切书，左侧导航进章节／概念／测验／诊断；进度存在本机浏览器，换设备不同步。

- 公式（KaTeX）与图（Mermaid）走 CDN，首次打开需要联网，之后有浏览器缓存。
- 离线时公式会退化成 TeX 源码，正文与导航不受影响。

## 部署到 GitHub Pages

在项目根目录（含 `index.html` 的这一层）执行：

```bash
git init
git add .
git commit -m "复分析可视化学习库"
git branch -M main
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git push -u origin main
```

然后到仓库 **Settings → Pages**：Source 选 *Deploy from a branch*，Branch 选 `main`，目录选 `/ (root)`，保存。一两分钟后访问：

```
https://<你的用户名>.github.io/<仓库名>/
```

`.nojekyll` 已放好，中文目录名与 `_` 开头的目录能原样托管。

## 目录结构

| 路径 | 说明 |
|---|---|
| `index.html` | 总入口（单文件，含全部页面与数据） |
| `index.md` | Markdown 导航 |
| `.nojekyll` | 关闭 Jekyll |
| `01-复分析可视化方法/` | 本书知识库：`chapters/`、`concepts/`、`manifest.json`、单书伴侣 HTML |
| `01-复分析可视化方法/_work/raw/` | 按章抽取的原文语料（过程产物） |
| `_build/` | 验证报告 |

## 进度说明

全书 12 章已完成：49 个概念页、25 份深度推导、101 道测验、98 张抽认卡、64 条术语。`manifest.json` 与各 Markdown 配套文件保持同步。
