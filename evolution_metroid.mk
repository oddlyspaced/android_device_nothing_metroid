# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Evolution X stuff.
# NOTE: Evolution X maps its vendor_evolution repo onto the vendor/lineage path,
# so this is Evo's common product config, not LineageOS's.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from metroid device
$(call inherit-product, device/nothing/metroid/device.mk)

# Qualcomm's vibrator product include adds the generic service independently.
# Keep only Nothing's stock AW86938/RichTap implementation.
PRODUCT_PACKAGES := $(filter-out vendor.qti.hardware.vibrator.service,$(PRODUCT_PACKAGES))

# Sign with our own release keys, not AOSP's public testkey (anyone can forge updates for that).
$(call inherit-product-if-exists, vendor/lineage-priv/keys/keys.mk)

PRODUCT_NAME := evolution_metroid
PRODUCT_DEVICE := metroid
PRODUCT_MANUFACTURER := Nothing
PRODUCT_BRAND := Nothing
PRODUCT_MODEL := Phone (3)

PRODUCT_GMS_CLIENTID_BASE := android-nothing
PRODUCT_SHIPPING_API_LEVEL := 35
