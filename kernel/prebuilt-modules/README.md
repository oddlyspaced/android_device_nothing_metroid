# Locally extracted kernel modules

Two GPL modules loaded by the stock `vendor_dlkm` image do not currently have
matching published source:

| Module | Purpose | Expected SHA-256 |
|---|---|---|
| `stm_nfc_i2c.ko` | ST NFC controller | `a7a8921eac43c8ca08bd4f486d1f00821a4ced4a0181dd4df5127198e6efffa3` |
| `stm_st54se_gpio.ko` | ST54 secure-element GPIO | `29433ecdc0f71acad76b71433c14a1b791f1b74e382b6ce6adc61132c0cda85b` |

Both expected files come from the `vendor_dlkm` partition of Nothing OS
`Metroid_B4.1-260814-1733` and report `6.6.127-android15-8`.

Nothing rebuilt both modules between `B4.0-250917-1218` (6.6.87) and this
release, so the hashes differ from the ones this file previously recorded. The
whole vendor blob set is extracted from `B4.1-260814-1733` -- the build
`BASELINE.md` requires for the modem -- so these are pinned to the same image
rather than mixing an older NFC module into a newer vendor set. The point-release
gap against the shipped 6.6.102 GKI `Image` is fine for the reason given in
`kernel/gki/README.md`: GKI enforces the KMI generation (`android15-8`), which
all three share, not the point release. This public
repository does not redistribute those binaries. Extract them from your own
copy of that documented stock image:

```bash
kernel/extract-unpublished-modules.sh /path/to/extracted/vendor_dlkm
```

The script verifies both hashes and writes them to the ignored
`kernel/local-prebuilt-modules/` directory consumed by
`stage_kernel_artifacts.sh`.

Redistributors remain responsible for satisfying all applicable license and
corresponding-source obligations. Local extraction is for private build and test
use; it does not by itself authorize public OTA redistribution. If matching
source is published, build these modules from source and remove the
local-extraction path.
