#!/bin/bash
# Regenerate series.conf and the patch files from the live tree.
#
# apply-series.sh consumes series.conf; this produces it. Every project holding a
# local branch named 'metroid' is walked, its pre-patch revision and result tree are
# recomputed, and format-patch is re-run. Run from anywhere; pass the Android tree root
# as $1 (default: four levels up from this script).
#
# Amending a carried commit without re-running this leaves series.conf recording a
# result tree that no longer exists, which apply-series.sh will reject.
set -u
TOP="${1:-$(cd "$(dirname "$0")/../../../.." && pwd)}"
cd "$TOP" || exit 1
P=device/nothing/metroid/patches

declare -A DIR
while IFS='|' read -r proj _pre _tree glob; do
  case "$proj" in \#*|"") continue;; esac
  DIR["$proj"]=$(echo "$glob" | sed 's#^patches/##; s#/\*\.patch$##')
done < "$P/series.conf"

TMP=$(mktemp)
echo "# project path | pre-patch revision | expected result tree | ordered patch glob" > "$TMP"
for proj in "${!DIR[@]}"; do
  d="$proj"; pd="${DIR[$proj]}"
  git -C "$d" show-ref --verify --quiet refs/heads/metroid || { echo "SKIP(no-branch)  $proj"; continue; }
  base=$(git -C "$d" rev-parse --verify --quiet metroid@{upstream} || git -C "$d" rev-parse --verify --quiet m/bka)
  [ -z "$base" ] && { echo "SKIP(no-base)    $proj"; continue; }
  n=$(git -C "$d" rev-list --count "$base"..metroid)
  [ "$n" = "0" ] && { echo "SKIP(no-commits) $proj"; continue; }
  pre=$(git -C "$d" rev-parse "metroid~$n")
  rtree=$(git -C "$d" rev-parse "metroid^{tree}")
  rm -rf "$P/$pd"; mkdir -p "$P/$pd"
  # default numbering + default signature: anything else makes every file show a spurious diff
  git -C "$d" format-patch -q -o "$TOP/$P/$pd" "metroid~$n..metroid" >/dev/null
  echo "$proj|$pre|$rtree|patches/$pd/*.patch" >> "$TMP"
  printf "%-46s n=%-2s -> patches/%s\n" "$proj" "$n" "$pd"
done
sort -t'|' -k1,1 "$TMP" -o "$TMP.s"; { head -1 "$TMP"; grep -v '^#' "$TMP.s"; } > "$P/series.conf"
rm -f "$TMP" "$TMP.s"
echo "series.conf: $(grep -vc '^#' "$P/series.conf") projects, $(find "$P" -name '*.patch' | wc -l) patches"
