#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 logix727
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

SOURCE="${1:?usage: $0 /path/to/extracted/vendor_dlkm}"
HERE="$(cd "$(dirname "$0")" && pwd)"
DEST="$HERE/local-prebuilt-modules"
TMP="$(mktemp -d "$HERE/.local-prebuilt-modules.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT

declare -A EXPECTED=(
    [stm_nfc_i2c.ko]=a7a8921eac43c8ca08bd4f486d1f00821a4ced4a0181dd4df5127198e6efffa3
    [stm_st54se_gpio.ko]=29433ecdc0f71acad76b71433c14a1b791f1b74e382b6ce6adc61132c0cda85b
)

for module in "${!EXPECTED[@]}"; do
    mapfile -t matches < <(find "$SOURCE" -type f -name "$module" -print)
    [[ ${#matches[@]} -eq 1 ]] || {
        echo "expected one $module under $SOURCE, found ${#matches[@]}" >&2
        exit 1
    }
    source_file="${matches[0]}"
    actual="$(sha256sum "$source_file" | cut -d' ' -f1)"
    [[ "$actual" == "${EXPECTED[$module]}" ]] || {
        echo "$module hash mismatch: expected ${EXPECTED[$module]}, got $actual" >&2
        exit 1
    }
    install -m 0644 "$source_file" "$TMP/$module"
done

rm -rf "$DEST"
mv "$TMP" "$DEST"
trap - EXIT
echo "Verified local modules in $DEST"
