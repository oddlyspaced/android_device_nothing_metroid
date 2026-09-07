# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

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

# Sign with our own release keys, not AOSP's public testkey (anyone can forge updates for that).
$(call inherit-product-if-exists, vendor/lineage-priv/keys/keys.mk)

PRODUCT_NAME := lineage_metroid
PRODUCT_DEVICE := metroid
PRODUCT_MANUFACTURER := Nothing
PRODUCT_BRAND := Nothing
PRODUCT_MODEL := Phone (3)

PRODUCT_GMS_CLIENTID_BASE := android-nothing
PRODUCT_SHIPPING_API_LEVEL := 35
