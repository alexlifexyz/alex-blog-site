# NOW

更新时间：2026-10-19

## 状态

- 线上：https://blog.alexai.top ，Cloudflare Pages 项目 `alex-blog` 连接 GitHub，合并到 main 自动发布。
- 2026-10-12 完成改版：视觉与主站统一，首页精选 + 分类筛选 + 按年分组，文章页目录、阅读进度、相关文章，搜索弹窗重写。
- 内容：80 篇文章，13 篇设为草稿，公开 67 篇。
- 2026-10-14 清理仓库（PR #2）：删除 wrangler 直传脚本和一次性的公众号同步脚本（重新运行会覆盖 10-12 手工清理过的文章）。
- 2026-10-14 去实名（PR #3）：站名改为「Alex 的博客」，字标换成云杉，页头页脚、作者栏、RSS 不再出现真实姓名和工作年限；分享图重做（照片保留）。

## 待定

- 精选里「十年 Java 架构师视角……」一篇与新口径（不写年限）冲突，另有 16 篇正文提到「十年 / 11 年」：Alex 手工处理。
- 3 月「降临派」旧稿（酱板鸭三部曲、IBM 量子霸权等热点改写）是否设为草稿。
- Cloudflare 上闲置的旧 Pages 项目 `alex-blog-site`（无域名）是否删除。

## 恢复

```bash
cd ~/studio/02-projects/alex-blog-site && git status && npm ci && npm run build
```

- 2026-10-17 PR #4：logo 换成帆影 A（与主站一致），favicon、Apple 图标、社交卡片同步，已上线。社交卡片上的副标题「Agent 与 RAG 落地、后端工程」还是旧定位，没改。

- 2026-10-19 博客迁到主站 `alexai.top/blog/`（主站 Decision 11）：挑了 20 篇有第一手内容、800 字以上的文章，清理后搬进 `alexlifexyz-site/src/content/posts`，以后在主站仓库写。本仓库分支 `chore/move-to-main-site`（未推送）把整站 301 到主站：`/posts/*` 按原 slug 跳，其余跳 `/blog/`。合并上线后本仓库归档（`studio archive`，Alex 确认）。
