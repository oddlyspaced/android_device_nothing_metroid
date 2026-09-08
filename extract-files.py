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



# Blobs built against an older frozen AIDL version than the platform now ships.
# Frozen AIDL versions are additive and ABI-stable, so the newest library exports
# everything the older one did. Remapping avoids Soong's 'multiple versions of the
# same aidl_interface' error, which fires when one module would pull both.
AIDL_VERSION_REMAP = {
    'android.hardware.security.sharedsecret-V2-ndk': 'android.hardware.security.sharedsecret-V1-ndk',
    'android.media.audio.common.types-V2-cpp': 'android.media.audio.common.types-V4-cpp',
}


def lib_fixup_aidl_version(lib: str, *args, **kwargs):
    return AIDL_VERSION_REMAP[lib]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'android.media.audio.common.types-V2-cpp',
        'android.hardware.security.sharedsecret-V2-ndk',
    ): lib_fixup_aidl_version,
    (
    ): lib_fixup_partition_suffix('system'),
    (
        'android.hardware.radio@1.5',
        'android.hardware.radio@1.6',
        'vendor.qti.ImsRtpService-V2-ndk',
        'vendor.qti.hardware.data.cneaidlservice.internal.server-V2-ndk',
        'vendor.qti.hardware.qteeconnector-V1-ndk',
    ): lib_fixup_partition_suffix('system_ext'),
    (
        'libOmxCore',
        'libOpenCL',
        'libbatching',
        'libgeofencing',
        'libgnss',
        'libgps.utils',
        'libloc_core',
        'liblocation_api',
        'liblogwrap',
        'libmemutils',
        'libmm-omxcore',
        'libplatformconfig',
        'libqti-perfd-client',
        'libstagefrighthw',
        'vendor.noth.hardware.camera-V1-ndk',
        'vendor.noth.hardware.charge-V1-ndk',
        'vendor.noth.hardware.stability-V1-ndk',
        'vendor.qti.ImsRtpService-V1-ndk',
        'vendor.qti.MemHal-V1-ndk',
        'vendor.qti.data.factoryservice-V1-ndk',
        'vendor.qti.data.mwqemaidlservice-V1-ndk',
        'vendor.qti.diaghal-V1-ndk',
        'vendor.qti.gnss-V7-ndk',
        'vendor.qti.hardware.ListenSoundModelAidl-V1-ndk',
        'vendor.qti.hardware.alarm-V1-ndk',
        'vendor.qti.hardware.bluetooth_sar-V1-ndk',
        'vendor.qti.hardware.bttpi-V3-ndk',
        'vendor.qti.hardware.c2pa-V1-ndk',
        'vendor.qti.hardware.cacertaidlservice-V1-ndk',
        'vendor.qti.hardware.capabilityconfigstore-V1-ndk',
        'vendor.qti.hardware.data.cneaidlservice.internal.api-V1-ndk',
        'vendor.qti.hardware.data.cneaidlservice.internal.constants-V1-ndk',
        'vendor.qti.hardware.data.cneaidlservice.internal.server-V1-ndk',
        'vendor.qti.hardware.data.connectionaidl-V1-ndk',
        'vendor.qti.hardware.data.connectionfactory-V1-ndk',
        'vendor.qti.hardware.data.dataactivity-V1-ndk',
        'vendor.qti.hardware.data.dynamicddsaidlservice-V1-ndk',
        'vendor.qti.hardware.data.flowaidlservice-V1-ndk',
        'vendor.qti.hardware.data.iwlandata-V2-ndk',
        'vendor.qti.hardware.data.ka-V1-ndk',
        'vendor.qti.hardware.data.lceaidlservice-V1-ndk',
        'vendor.qti.hardware.data.qmiaidlservice-V1-ndk',
        'vendor.qti.hardware.dpmaidlservice-V1-ndk',
        'vendor.qti.hardware.dsp-V1-ndk',
        'vendor.qti.hardware.embmsslaidl-V2-ndk',
        'vendor.qti.hardware.fm-V1-ndk',
        'vendor.qti.hardware.hexlp-V1-ndk',
        'vendor.qti.hardware.minkipcbinder-V1-ndk',
        'vendor.qti.hardware.mwqemadapteraidlservice-V1-ndk',
        'vendor.qti.hardware.perf2-V1-ndk',
        'vendor.qti.hardware.power.powermodule-V1-ndk',
        'vendor.qti.hardware.qasr-V2-ndk',
        'vendor.qti.hardware.qconfig-V1-ndk',
        'vendor.qti.hardware.qseecom-V1-ndk',
        'vendor.qti.hardware.qxr-V2-ndk',
        'vendor.qti.hardware.radio.am-V1-ndk',
        'vendor.qti.hardware.radio.atfwd-V1-ndk',
        'vendor.qti.hardware.radio.common-V1-ndk',
        'vendor.qti.hardware.radio.ims-V16-ndk',
        'vendor.qti.hardware.radio.internal.deviceinfo-V1-ndk',
        'vendor.qti.hardware.radio.lpa-V1-ndk',
        'vendor.qti.hardware.radio.qcrilhook-V1-ndk',
        'vendor.qti.hardware.radio.qtiradio-V16-ndk',
        'vendor.qti.hardware.radio.qtiradioconfig-V6-ndk',
        'vendor.qti.hardware.radio.uim-V1-ndk',
        'vendor.qti.hardware.radio.uim_remote_client-V1-ndk',
        'vendor.qti.hardware.radio.uim_remote_server-V1-ndk',
        'vendor.qti.hardware.secureprocessor.common-V1-ndk',
        'vendor.qti.hardware.secureprocessor.config-V1-ndk',
        'vendor.qti.hardware.secureprocessor.device-V1-ndk',
        'vendor.qti.hardware.sensorscalibrate-V1-ndk',
        'vendor.qti.hardware.sigma_miracast_aidl-V1-ndk',
        'vendor.qti.hardware.spu-V2-ndk',
        'vendor.qti.hardware.trustedui-V1-ndk',
        'vendor.qti.hardware.vpp-V1-ndk',
        'vendor.qti.hardware.wifi.wifilearner-V1-ndk',
        'vendor.qti.hardware.wifidisplaysession_aidl-V1-ndk',
        'vendor.qti.ims.callcapabilityaidlservice-V1-ndk',
        'vendor.qti.ims.configaidlservice-V1-ndk',
        'vendor.qti.ims.connectionaidlservice-V1-ndk',
        'vendor.qti.ims.factoryaidlservice-V1-ndk',
        'vendor.qti.ims.imscmaidlservice-V1-ndk',
        'vendor.qti.ims.rcssipaidlservice-V1-ndk',
        'vendor.qti.ims.rcsuceaidlservice-V1-ndk',
        'vendor.qti.ims.uceaidlservice-V1-ndk',
        'vendor.qti.latencyaidlservice-V1-ndk',
        'vendor.qti.memory.pasrmanager-V1-ndk',
        'vendor.qti.qccsyshal_aidl-V1-ndk',
        'vendor.qti.qccvndhal_aidl-V1-ndk',
        'vendor.qti.qesdhalaidl-V2-ndk',
        'vendor.qti.qspmhal-V1-ndk',
        'vendor.qti.snapdragonServices-V1-ndk',
        'vendor.qti.snapdragonServices.qape-V1-ndk',
        'vendor.qti.syshealthmon-V1-ndk',
    ): lib_fixup_partition_suffix('vendor'),
}

namespace_imports = [
    'hardware/qcom-caf/sm8750',
    'hardware/qcom-caf/wlan',
    # libwifi-hal-ctrl et al live in the NESTED namespace declared at
    # hardware/qcom-caf/wlan/qcwcn/Android.bp; importing the parent does not reach them.
    'hardware/qcom-caf/wlan/qcwcn',
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
    # Nothing ships this with <?xml version="2.0"?>. There is no XML 2.0, so the
    # xmllint the build runs over every copied XML rejects it and the copy fails.
    # It is the only malformed XML of the 320 staged blobs.
    'system_ext/etc/permissions/vendor.qti.hardware.c2pa-V1-java.xml': blob_fixup()
        .regex_replace('<\\?xml version="2\\.0"', '<?xml version="1.0"'),
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
