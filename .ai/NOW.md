# NOW

更新时间：2026-10-14

## 状态

- 线上：https://blog.alexai.top ，Cloudflare Pages 项目 `alex-blog` 连接 GitHub，合并到 main 自动发布。
- 2026-10-12 完成改版：视觉与主站统一，首页精选 + 分类筛选 + 按年分组，文章页目录、阅读进度、相关文章，搜索弹窗重写。
- 内容：80 篇文章，13 篇设为草稿，公开 67 篇。
- 2026-10-14 清理仓库：删除 wrangler 直传脚本和一次性的公众号同步脚本（重新运行会覆盖 10-12 手工清理过的文章）。

## 待定

- 3 月「降临派」旧稿（酱板鸭三部曲、IBM 量子霸权等热点改写）是否设为草稿。
- Cloudflare 上闲置的旧 Pages 项目 `alex-blog-site`（无域名）是否删除。

## 恢复

```bash
cd ~/studio/02-projects/alex-blog-site && git status && npm ci && npm run build
```
