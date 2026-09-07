#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)


def lib_fixup_partition_suffix(partition: str):
    def fixup(lib: str, *args, **kwargs):
        return f'{lib}_{partition}'
    return fixup


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'android.media.audio.common.types-V2-cpp',
        'libmdnssd',
    ): lib_fixup_partition_suffix('system'),
    (
        'android.hardware.radio@1.5',
        'android.hardware.radio@1.6',
        'android.hidl.base@1.0',
        'libaudiohalvendorextn',
        'libdisplayconfig.system.qti',
        'libencoderjpeg_jni',
        'libgralloc.system.qti',
        'libqcomfm_jni',
        'libqti_vndfwk_detect_system',
        'libvndfwk_detect_jni.qti_system',
        'vendor.qti.hardware.capabilityconfigstore@1.0',
        'vendor.qti.hardware.display.composer@3.0',
        'vendor.qti.hardware.display.composer@3.1',
        'vendor.qti.hardware.perf@2.3',
    ): lib_fixup_partition_suffix('system_ext'),
    (
        'android.frameworks.sensorservice@1.0',
        'android.hardware.audio.common-V3-ndk',
        'android.hardware.audio.common@5.0',
        'android.hardware.audio.effect-V2-ndk',
        'android.hardware.authsecret@1.0',
        'android.hardware.automotive.vehicle@2.0',
        'android.hardware.automotive.vehicle@2.0-manager-lib',
        'android.hardware.bluetooth.audio-V4-ndk',
        'android.hardware.bluetooth.audio-impl',
        'android.hardware.bluetooth.audio@2.0',
        'android.hardware.bluetooth.audio@2.1',
        'android.hardware.bluetooth@1.0',
        'android.hardware.boot@1.0',
        'android.hardware.boot@1.1',
        'android.hardware.gatekeeper@1.0',
        'android.hardware.graphics.allocator@2.0',
        'android.hardware.graphics.allocator@3.0',
        'android.hardware.graphics.allocator@4.0',
        'android.hardware.graphics.bufferqueue@1.0',
        'android.hardware.graphics.bufferqueue@2.0',
        'android.hardware.graphics.common@1.0',
        'android.hardware.graphics.common@1.1',
        'android.hardware.graphics.common@1.2',
        'android.hardware.graphics.composer@2.1',
        'android.hardware.graphics.composer@2.2',
        'android.hardware.graphics.composer@2.3',
        'android.hardware.graphics.mapper@2.0',
        'android.hardware.graphics.mapper@2.1',
        'android.hardware.graphics.mapper@3.0',
        'android.hardware.graphics.mapper@4.0',
        'android.hardware.health@1.0',
        'android.hardware.health@2.0',
        'android.hardware.health@2.1',
        'android.hardware.keymaster@3.0',
        'android.hardware.keymaster@4.0',
        'android.hardware.keymaster@4.1',
        'android.hardware.media.bufferpool@2.0',
        'android.hardware.media.c2@1.0',
        'android.hardware.media.omx@1.0',
        'android.hardware.media@1.0',
        'android.hardware.power@1.0',
        'android.hardware.power@1.1',
        'android.hardware.power@1.2',
        'android.hardware.radio@1.0',
        'android.hardware.radio@1.1',
        'android.hardware.renderscript@1.0',
        'android.hardware.secure_element@1.0',
        'android.hardware.secure_element@1.1',
        'android.hardware.secure_element@1.2',
        'android.hardware.security.keymint-V3-ndk',
        'android.hardware.sensors-V2-ndk',
        'android.hardware.sensors@1.0',
        'android.hardware.sensors@2.0',
        'android.hardware.sensors@2.0-ScopedWakelock',
        'android.hardware.sensors@2.1',
        'android.hardware.thermal@1.0',
        'android.hardware.thermal@2.0',
        'android.hardware.usb.gadget@1.0',
        'android.hardware.usb.gadget@1.1',
        'android.hidl.allocator@1.0',
        'android.hidl.memory.token@1.0',
        'android.hidl.memory@1.0',
        'android.hidl.safe_union@1.0',
        'android.hidl.token@1.0',
        'android.hidl.token@1.0-utils',
        'android.media.audio.common.types-V3-ndk',
        'android.system.wifi.keystore@1.0',
        'com.dsi.ant@1.0',
        'libOmxCore',
        'libOpenCL',
        'libPeripheralStateUtils',
        'libRSCpuRef',
        'libRSDriver',
        'libRS_internal',
        'lib_android_keymaster_keymint_utils',
        'lib_bt_aptx',
        'lib_bt_ble',
        'lib_bt_bundle',
        'libaconfig_storage_read_api_cc',
        'libagm',
        'libagm_compress_plugin',
        'libagm_mixer_plugin',
        'libagm_pcm_plugin',
        'libagmclient',
        'libagmipcservice',
        'libalsautils',
        'libalsautilsv2',
        'libandroid_runtime_lazy',
        'libar-acdb',
        'libar-gpr',
        'libar-gsl',
        'libar-pal',
        'libats',
        'libaudio_aidl_conversion_common_ndk',
        'libaudiochargerlistener',
        'libaudioplatformconverter.qti',
        'libaudioroute',
        'libaudioserviceexampleimpl',
        'libaudioutils',
        'libavservices_minijail',
        'libbatching',
        'libbatterylistener',
        'libbcinfo',
        'libbinder',
        'libbinderdebug',
        'libblas',
        'libbluetooth_audio_session',
        'libbluetooth_audio_session_aidl',
        'libcamera2ndk_vendor',
        'libcamera_metadata',
        'libcap',
        'libchrome',
        'libcld80211',
        'libcodec2',
        'libcodec2_aidl',
        'libcodec2_hal_common',
        'libcodec2_hidl@1.0',
        'libcodec2_hidl_plugin',
        'libcodec2_vndk',
        'libcompiler_rt',
        'libcppbor',
        'libcppbor_external',
        'libcppcose_rkp',
        'libcrypto',
        'libcurl',
        'libcustomva_intf',
        'libdisplayconfig.qti',
        'libdisplaydebug',
        'libdmabufheap',
        'libdrm',
        'libdrmutils',
        'libeffects',
        'libeffectsconfig',
        'libevent',
        'libexif',
        'libexpat',
        'libfilefinder',
        'libflatbuffers-cpp',
        'libfmpal',
        'libfmq',
        'libgatekeeper',
        'libgeofencing',
        'libgnss',
        'libgps.utils',
        'libgpu_tonemapper',
        'libgralloc.qti',
        'libgralloccore',
        'libgralloctypes',
        'libgrallocutils',
        'libhardware',
        'libhardware_legacy',
        'libhfp_pal',
        'libhidlbase',
        'libhidlmemory',
        'libhidltransport',
        'libhidparser',
        'libhistogram',
        'libhotword_intf',
        'libhwbinder',
        'libion',
        'libipanat',
        'libjpeg',
        'libjson',
        'libjsoncpp',
        'libkeymaster_messages',
        'libkeymaster_portable',
        'libkeystore-engine-wifi-hidl',
        'libkeystore-wifi-hidl',
        'libloc_core',
        'liblocation_api',
        'liblogwrap',
        'liblx-ar_util',
        'liblx-osal',
        'liblzma',
        'libmapperutils',
        'libmedia_helper',
        'libmediautils_vendor',
        'libmemunreachable',
        'libmemutils',
        'libminijail',
        'libmm-omxcore',
        'libnbaio_mono',
        'libnetfilter_conntrack',
        'libnetutils',
        'libnfnetlink',
        'libnl',
        'liboffloadhal',
        'libpalclient',
        'libpaleventnotifier',
        'libpalipcservice',
        'libpasn',
        'libplatformconfig',
        'libpng',
        'libpower',
        'libprocessgroup',
        'libpsi',
        'libqdMetaData',
        'libqdutils',
        'libqservice',
        'libqti-perfd-client',
        'libqti_vndfwk_detect',
        'libqti_vndfwk_detect_vendor',
        'libqtivibratoreffect',
        'libqtivibratoreffectoffload',
        'libreference-ril',
        'libril',
        'librilutils',
        'librmnetctl',
        'libsdedrm',
        'libsdmclient',
        'libsdmcore',
        'libsdmdal',
        'libsdmutils',
        'libsensorndkbridge',
        'libsgutils2',
        'libsndcardparser',
        'libsoft_attestation_cert',
        'libspeexresampler',
        'libsqlite',
        'libssl',
        'libstagefright_aidl_bufferpool2',
        'libstagefright_bufferpool@2.0.1',
        'libstagefright_bufferqueue_helper',
        'libstagefright_foundation',
        'libstagefrighthw',
        'libtensorflowlite_c',
        'libtinyalsa',
        'libtinyalsav2',
        'libtinycompress',
        'libtinyxml2',
        'libui',
        'libunwindstack',
        'libusbhost',
        'libutils',
        'libutilscallstack',
        'libvibratorutils',
        'libvmmem',
        'libvndfwk_detect_jni.qti',
        'libvndfwk_detect_jni.qti_vendor',
        'libvui_intf',
        'libwfdaac_vendor',
        'libwifi-hal',
        'libwifi-hal-ctrl',
        'libwifi-hal-qcom',
        'libwifi-system-iface',
        'libwpa_client',
        'libxml2',
        'libz',
        'server_configurable_flags',
        'vendor.display.config@1.0',
        'vendor.display.config@1.1',
        'vendor.display.config@1.10',
        'vendor.display.config@1.11',
        'vendor.display.config@1.2',
        'vendor.display.config@1.3',
        'vendor.display.config@1.4',
        'vendor.display.config@1.5',
        'vendor.display.config@1.6',
        'vendor.display.config@1.7',
        'vendor.display.config@1.8',
        'vendor.display.config@1.9',
        'vendor.display.config@2.0',
        'vendor.qti.hardware.bluetooth_audio@2.0',
        'vendor.qti.hardware.bluetooth_audio@2.1',
        'vendor.qti.hardware.display.allocator@1.0',
        'vendor.qti.hardware.display.allocator@3.0',
        'vendor.qti.hardware.display.allocator@4.0',
        'vendor.qti.hardware.display.composer@1.0',
        'vendor.qti.hardware.display.composer@2.0',
        'vendor.qti.hardware.display.mapper@1.0',
        'vendor.qti.hardware.display.mapper@1.1',
        'vendor.qti.hardware.display.mapper@2.0',
        'vendor.qti.hardware.display.mapper@3.0',
        'vendor.qti.hardware.display.mapper@4.0',
        'vendor.qti.hardware.display.mapperextensions@1.0',
        'vendor.qti.hardware.display.mapperextensions@1.1',
        'vendor.qti.hardware.display.mapperextensions@1.2',
        'vendor.qti.hardware.display.mapperextensions@1.3',
        'vendor.qti.hardware.display.snapalloc-impl',
        'vendor.qti.hardware.perf@2.0',
        'vendor.qti.hardware.perf@2.1',
        'vendor.qti.hardware.perf@2.2',
        'vendor.qti.hardware.servicetracker@1.0',
        'vendor.qti.hardware.servicetracker@1.1',
        'vendor.qti.hardware.systemhelper@1.0',
        'vendor.qti.hardware.vibrator.impl',
        'vendor.qti.hardware.vibratorCL.impl',
        'vendor.qti.hardware.vibratorOL.impl',
        'vendor.qti.hardware.vibratorSel.impl',
        'wifi_legacy',
        'android.hardware.security.sharedsecret-V2-ndk',
        'android.media.audio.common.types-V2-ndk',
        'android.hardware.graphics.common-V5-ndk',
        'vendor.qti.hardware.display.config-V5-ndk',
        'android.hardware.graphics.allocator-V1-ndk',
        'android.hardware.audio.core.sounddose-V1-ndk',
        'android.hardware.audio.core.sounddose-V2-ndk',
        'android.hardware.audio.core-V2-ndk',
    ): lib_fixup_partition_suffix('vendor'),
}

namespace_imports = [
    'hardware/qcom-caf/sm8750',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
    'device/nothing/metroid',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/android.hardware.biometrics.face-service.noth.rc': blob_fixup()
        .regex_replace('    disabled\n    disabled\n', '    disabled\n')
        .regex_replace(
            '    group camera system\n',
            '    group camera system\n'
            '    interface aidl android.hardware.biometrics.face.IFace/default\n',
        ),
    'vendor/etc/init/cnd.rc': blob_fixup()
        .regex_replace('    disabled\n', ''),
    'vendor/etc/init/qms.rc': blob_fixup()
        .regex_replace('    disabled\n', '')
        .regex_replace(
            '     class main\n',
            '     class main\n'
            '     user root\n',
        )
        .regex_replace('    user root\n    group root\n', ''),
    'vendor/etc/init/init.nt_logtool.rc': blob_fixup()
        .regex_replace(
            'service diag_gpslog_start ',
            'on post-fs-data\n'
            '    mkdir /data/vendor/diag_mdlog 0770 root system\n'
            '    restorecon_recursive /data/vendor/diag_mdlog\n\n'
            'service diag_gpslog_start ',
        ),
    'system_ext/etc/init/perfservice.rc': blob_fixup()
        .regex_replace(
            'service vendor.perfservice /system_ext/bin/perfservice\n'
            '    class main\n'
            '    user system\n'
            '    group system readproc\n\n',
            '',
        ),
    'vendor/etc/init/hw/init.qcom.usb.rc': blob_fixup()
        .regex_replace('ncm\\.0', 'ncm.gs6'),
    'vendor/etc/init/hw/init.qcom.rc': blob_fixup()
        .regex_replace(
            '    exec u:r:vendor_qti_init_shell:s0 -- /vendor/bin/init\\.qti\\.can\\.sh\n',
            '',
        )
        .regex_replace(
            'service nqnfcinfo /system/vendor/bin/nqnfcinfo\n'
            '    class late_start\n'
            '    group nfc\n'
            '    user system\n'
            '    oneshot\n\n',
            '',
        )
        .regex_replace(
            'service ptt_socket_app /system/vendor/bin/ptt_socket_app -d\n'
            '    class main\n'
            '    user wifi\n'
            '    group wifi system inet net_admin\n'
            '    capabilities NET_ADMIN\n'
            '    oneshot\n\n',
            '',
        )
        .regex_replace(
            'service qvop-daemon /vendor/bin/qvop-daemon\n'
            '    class late_start\n'
            '    user system\n'
            '    group system drmrpc\n\n',
            '',
        )
        .regex_replace(
            'service qseeproxydaemon /system/vendor/bin/qseeproxydaemon\n'
            '    class late_start\n'
            '    user system\n'
            '    group system\n\n',
            '',
        )
        .regex_replace(
            'service vendor\\.atfwd /vendor/bin/ATFWD-daemon\n'
            '    class late_start\n'
            '    user system\n'
            '    group system radio\n\n',
            '',
        )
        .regex_replace(
            'service esepmdaemon /system/vendor/bin/esepmdaemon\n'
            '    class core\n'
            '    user system\n'
            '    group nfc\n\n',
            '',
        )
        .regex_replace(
            'service chre /vendor/bin/chre\n'
            '    class late_start\n'
            '    user system\n'
            '    group system\n'
            '    socket chre seqpacket 0660 root system\n'
            '    shutdown critical\n\n'
            'on property:vendor\\.chre\\.enabled=0\n'
            '   stop chre\n\n',
            '',
        ),
    'vendor/etc/init/vendor.qti.hardware.perf2-hal-service.rc': blob_fixup()
        .regex_replace('    disabled\n    disabled\n', ''),
    'vendor/etc/init/vendor.qti.media.c2@1.0-service.rc': blob_fixup()
        .regex_replace('    disabled\n', ''),
    'vendor/etc/init/vendor.qti.media.c2audio@1.0-service.rc': blob_fixup()
        .regex_replace('    disabled\n', ''),
}

module = ExtractUtilsModule(
    'metroid',
    'nothing',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
