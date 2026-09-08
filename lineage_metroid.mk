# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Pico GMS, not full. metroid's super partition is 8.50 GiB and stock already fills
# 99.25% of it (9058279424 of 9126805504), so there is essentially no room to grow.
# Full GMS adds 2.09 GiB of apps and overflows the super by 2.33 GiB. Pico keeps
# Phonesky, GmsCore and GoogleServicesFramework -- Play Store works, and everything it
# drops (Velvet, Photos, Recorder, ARCore, the Pixel wallpapers) reinstalls from Play.
# Must be set BEFORE common_full_phone.mk, which reads it to pick the gms_*.mk variant.
TARGET_USES_PICO_GAPPS := true

# Inherit some common Lineage stuff.
# NOTE: on an Evolution X tree this resolves to Evo's own config -- Evo checks its
# vendor_evolution repo out at vendor/lineage and reuses the Lineage build system.
# The lineage_ product prefix is required, not cosmetic: vendor/lineage/build/envsetup.sh
# only sets LINEAGE_BUILD for products matching ^lineage_, and build/make/core/config.mk
# gates the include of BoardConfigLineage.mk (kernel, qcom and Soong var exports) on it.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from metroid device
$(call inherit-product, device/nothing/metroid/device.mk)

# Qualcomm's vibrator product include adds the generic service independently.
# Keep only Nothing's stock AW86938/RichTap implementation.
PRODUCT_PACKAGES := $(filter-out vendor.qti.hardware.vibrator.service,$(PRODUCT_PACKAGES))

# Same for thermal. The real fix is the soong_config guard on the source module
# (metroid.stock_thermal, set in device.mk) -- filtering PRODUCT_PACKAGES alone does
# NOT stop it building, because the source HAL is pulled in independently. Both install
# under the same stem, so ninja fails with dupbuild=err on the symbols path. The stock
# blob carries Nothing's shell_max mapping and thresholds. This line is belt-and-braces.
PRODUCT_PACKAGES := $(filter-out android.hardware.thermal-service.qti,$(PRODUCT_PACKAGES))

# Sign with our own release keys, not AOSP's public testkey (anyone can forge updates for that).
$(call inherit-product-if-exists, vendor/lineage-priv/keys/keys.mk)

PRODUCT_NAME := lineage_metroid
PRODUCT_DEVICE := metroid
PRODUCT_MANUFACTURER := Nothing
PRODUCT_BRAND := Nothing
PRODUCT_MODEL := Phone (3)

PRODUCT_GMS_CLIENTID_BASE := android-nothing
PRODUCT_SHIPPING_API_LEVEL := 35
