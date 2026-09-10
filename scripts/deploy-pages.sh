#!/usr/bin/env bash
set -e

# 定位项目根目录
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# 载入 .env
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# 自动检测本地 Clash 代理端口
if nc -z 127.0.0.1 7897 2>/dev/null; then
  export https_proxy="http://127.0.0.1:7897"
  export http_proxy="http://127.0.0.1:7897"
elif nc -z 127.0.0.1 7890 2>/dev/null; then
  export https_proxy="http://127.0.0.1:7890"
  export http_proxy="http://127.0.0.1:7890"
fi

echo "开始构建全站与全文本搜索索引..."
npm run build

echo "正在直传部署到 Cloudflare Pages..."
npx wrangler pages deploy dist --project-name alex-blog-site "$@"
