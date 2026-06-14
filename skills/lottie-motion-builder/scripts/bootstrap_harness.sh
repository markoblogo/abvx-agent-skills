#!/usr/bin/env bash
set -euo pipefail

repo_url="https://github.com/diffusionstudio/lottie.git"
target_dir="${1:-$HOME/.codex/vendor/diffusionstudio-lottie}"

mkdir -p "$(dirname "$target_dir")"

if [ -d "$target_dir/.git" ]; then
  git -C "$target_dir" fetch --depth=1 origin main
  git -C "$target_dir" reset --hard origin/main
else
  rm -rf "$target_dir"
  git clone --depth=1 "$repo_url" "$target_dir"
fi

printf 'Harness ready at %s\n' "$target_dir"
printf 'Next steps:\n'
printf '  cd %s\n' "$target_dir"
printf '  npm install\n'
printf '  npm run dev\n'
