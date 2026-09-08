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
        'vendor.qti.hardware.camera.aon-V1-ndk',
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
        'vendor.qti.hardware.wifi.supplicant-V1-ndk',
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
        'qti-audio-types-aidl-V1-ndk',
        'vendor.qti.hardware.camera.aon-V2-ndk',
        'vendor.qti.hardware.display.aiqe-V2-ndk',
        'vendor.qti.hardware.display.color-V1-ndk',
        'vendor.qti.hardware.display.postproc-V1-ndk',
        'vendor.qti.hardware.display.demura-V1-ndk',
        'android.hardware.security.rkp-V3-ndk',
        'android.hardware.memtrack-V1-ndk',
        'android.hardware.authsecret-V1-ndk',
        'android.hardware.light-V2-ndk',
        'android.hardware.security.secureclock-V1-ndk',
        'libcodec2_hidl@1.0',
        'android.hardware.weaver-V2-ndk',
        'android.hardware.nfc-V1-ndk',
        'android.automotive.watchdog-V2-ndk',
        'android.hardware.boot-V1-ndk',
        'android.hardware.keymaster-V3-ndk',
        'android.hardware.bluetooth.finder-V1-ndk',
        'android.hardware.biometrics.common-V3-ndk',
        'android.system.net.netd-V1-ndk',
        'android.system.suspend-V1-ndk',
        'android.hardware.thermal-V1-ndk',
        'android.hardware.usb.gadget-V1-ndk',
        'android.hardware.thermal-V2-ndk',
        'android.hardware.keymaster-V4-ndk',
        'android.hardware.tetheroffload-V1-ndk',
        'android.frameworks.cameraservice.common-V1-ndk',
        'android.se.omapi-V1-ndk',
        'android.hardware.usb-V1-ndk',
        'android.hardware.identity-V5-ndk',
        'android.hardware.wifi.common-V1-ndk',
        'android.hardware.drm-V1-ndk',
        'vendor.qti.hardware.display.config-V1-ndk',
        'android.hardware.security.keymint-V2-ndk',
        'vendor.qti.hardware.paleventnotifier-V2-ndk',
        'android.hardware.security.keymint-V1-ndk',
        'vendor.qti.hardware.display.config-V2-ndk',
        'android.hardware.security.keymint-V3-ndk',
        'vendor.qti.hardware.qspa-V1-ndk',
        'vendor.qti.hardware.display.config-V3-ndk',
        'android.hardware.biometrics.fingerprint-V3-ndk',
        'vendor.qti.hardware.display.config-V4-ndk',
        'android.hardware.wifi.supplicant-V3-ndk',
        'vendor.qti.hardware.systemhelperaidl-V1-ndk',
        'vendor.qti.hardware.display.config-V5-ndk',
        'vendor.qti.hardware.display.config-V6-ndk',
        'vendor.qti.hardware.display.config-V7-ndk',
        'vendor.qti.hardware.display.config-V8-ndk',
        'vendor.qti.hardware.display.config-V9-ndk',
        'vendor.qti.hardware.display.config-V10-ndk',
        'vendor.qti.hardware.display.config-V11-ndk',
        'vendor.qti.hardware.display.config-V12-ndk',
        'android.hardware.wifi.hostapd-V2-ndk',
        'android.hardware.wifi-V2-ndk',
        'android.hardware.power-V5-ndk',
        'android.hardware.graphics.allocator-V1-ndk',
        'android.hardware.media.bufferpool2-V2-ndk',
        'android.hardware.graphics.allocator-V2-ndk',
        'android.frameworks.cameraservice.device-V2-ndk',
        'android.hardware.gatekeeper-V1-ndk',
        'android.system.keystore2-V1-ndk',
        'vendor.qti.hardware.camera.offlinecamera-V1-ndk',
        'vendor.qti.hardware.display.composer3-V1-ndk',
        'vendor.qti.hardware.servicetrackeraidl-V1-ndk',
        'vendor.qti.hardware.bluetooth.audio-V1-ndk',
        'vendor.qti.hardware.camera.offlinecamera-V2-ndk',
        'android.hardware.power.stats-V2-ndk',
        'android.hardware.media.c2-V1-ndk',
        'android.frameworks.cameraservice.service-V2-ndk',
        'android.hardware.bluetooth-V1-ndk',
        'android.hardware.camera.metadata-V2-ndk',
        'vendor.qti.hardware.display.composer3-V2-ndk',
        'vendor.qti.hardware.display.composer3-V3-ndk',
        'android.hardware.radio.sap-V1-ndk',
        'android.hardware.bluetooth.lmp_event-V1-ndk',
        'android.hardware.radio-V3-ndk',
        'android.hardware.health-V1-ndk',
        'android.hardware.camera.common-V1-ndk',
        'android.hardware.health-V3-ndk',
        'android.media.soundtrigger.types-V1-ndk',
        'android.hardware.secure_element-V1-ndk',
        'android.hardware.gnss-V4-ndk',
        'android.media.audio.common.types-V2-ndk',
        'android.media.audio.common.types-V3-ndk',
        'android.hardware.radio.data-V3-ndk',
        'android.frameworks.location.altitude-V2-ndk',
        'android.hardware.radio.modem-V3-ndk',
        'android.hardware.radio.messaging-V3-ndk',
        'android.hardware.radio.voice-V3-ndk',
        'android.hardware.vibrator-V2-ndk',
        'android.hardware.graphics.common-V5-ndk',
        'android.hardware.graphics.composer@2.1',
        'android.hardware.radio.config-V3-ndk',
        'android.hardware.radio.network-V3-ndk',
        'android.hardware.audio.common@5.0',
        'android.hardware.audio.common-V2-ndk',
        'android.hardware.camera.device-V2-ndk',
        'android.hardware.audio.core.sounddose-V1-ndk',
        'android.hardware.audio.core.sounddose-V2-ndk',
        'android.hardware.audio.common-V3-ndk',
        'android.hardware.sensors-V2-ndk',
        'android.hardware.soundtrigger3-V1-ndk',
        'android.hardware.graphics.composer3-V2-ndk',
        'android.hardware.graphics.composer3-V3-ndk',
        'android.hardware.common-V2-ndk',
        'android.hardware.bluetooth.audio-V3-ndk',
        'android.hardware.audio.effect-V2-ndk',
        'vendor.qti.hardware.display.mapperextensions@1.2',
        'android.hardware.radio.sim-V3-ndk',
        'android.hardware.bluetooth.audio-V4-ndk',
        'android.hardware.common.fmq-V1-ndk',
        'vendor.qti.hardware.systemhelper@1.0',
        'android.hardware.secure_element@1.2',
        'android.frameworks.sensorservice@1.0',
        'android.frameworks.sensorservice-V1-ndk',
        'android.hardware.audio.core-V2-ndk',
        'android.hardware.authsecret@1.0',
        'android.hardware.automotive.vehicle@2.0',
        'android.hardware.bluetooth.audio@2.0',
        'android.hardware.bluetooth.audio@2.1',
        'android.hardware.bluetooth@1.0',
        'android.hardware.boot@1.0',
        'android.hardware.boot@1.1',
        'android.hardware.camera.provider-V2-ndk',
        'android.hardware.gatekeeper@1.0',
        'android.hardware.graphics.allocator@2.0',
        'android.hardware.graphics.allocator@3.0',
        'android.hardware.graphics.allocator@4.0',
        'android.hardware.graphics.bufferqueue@1.0',
        'android.hardware.graphics.bufferqueue@2.0',
        'android.hardware.graphics.common@1.0',
        'android.hardware.graphics.common@1.1',
        'android.hardware.graphics.common@1.2',
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
        'android.hardware.sensors@1.0',
        'android.hardware.sensors@2.0',
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
        'android.system.wifi.keystore@1.0',
        'com.dsi.ant@1.0',
        'com.qualcomm.qti.dpm.api@1.0',
        'com.qualcomm.qti.imscmservice@1.0',
        'com.qualcomm.qti.imscmservice@2.0',
        'com.qualcomm.qti.imscmservice@2.1',
        'com.qualcomm.qti.imscmservice@2.2',
        'com.qualcomm.qti.uceservice@2.0',
        'com.qualcomm.qti.uceservice@2.1',
        'com.qualcomm.qti.uceservice@2.2',
        'com.qualcomm.qti.uceservice@2.3',
        'vendor.display.color@1.0',
        'vendor.display.color@1.1',
        'vendor.display.color@1.2',
        'vendor.display.color@1.3',
        'vendor.display.color@1.4',
        'vendor.display.color@1.5',
        'vendor.display.color@1.6',
        'vendor.display.color@1.7',
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
        'vendor.display.postproc@1.0',
        'vendor.noth.hardware.wifi.supplicant-V1-ndk',
        'vendor.qti.data.mwqem@1.0',
        'vendor.qti.data.slm@1.0',
        'vendor.qti.diaghal@1.0',
        'vendor.qti.esepowermanager@1.0',
        'vendor.qti.hardware.agm-V1-ndk',
        'vendor.qti.hardware.automotive.vehicle@1.0',
        'vendor.qti.hardware.bluetooth_audio@2.0',
        'vendor.qti.hardware.bluetooth_audio@2.1',
        'vendor.qti.hardware.data.connection@1.0',
        'vendor.qti.hardware.data.connection@1.1',
        'vendor.qti.hardware.data.dynamicdds@1.0',
        'vendor.qti.hardware.data.dynamicdds@1.1',
        'vendor.qti.hardware.data.flow@1.0',
        'vendor.qti.hardware.data.flow@1.1',
        'vendor.qti.hardware.data.latency@1.0',
        'vendor.qti.hardware.data.lce@1.0',
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
        'vendor.qti.hardware.display.mapperextensions@1.3',
        'vendor.qti.hardware.fingerprint@1.0',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.hardware.iop@1.0',
        'vendor.qti.hardware.iop@2.0',
        'vendor.qti.hardware.pal-V1-ndk',
        'vendor.qti.hardware.perf@2.0',
        'vendor.qti.hardware.perf@2.1',
        'vendor.qti.hardware.perf@2.2',
        'vendor.qti.hardware.qdutils_disp@1.0',
        'vendor.qti.hardware.qseecom@1.0',
        'vendor.qti.hardware.qteeconnector@1.0',
        'vendor.qti.hardware.radio.am@1.0',
        'vendor.qti.hardware.radio.atcmdfwd@1.0',
        'vendor.qti.hardware.radio.ims@1.0',
        'vendor.qti.hardware.radio.ims@1.1',
        'vendor.qti.hardware.radio.ims@1.2',
        'vendor.qti.hardware.radio.ims@1.3',
        'vendor.qti.hardware.radio.ims@1.4',
        'vendor.qti.hardware.radio.ims@1.5',
        'vendor.qti.hardware.radio.ims@1.6',
        'vendor.qti.hardware.radio.ims@1.7',
        'vendor.qti.hardware.radio.ims@1.8',
        'vendor.qti.hardware.radio.lpa@1.0',
        'vendor.qti.hardware.radio.lpa@1.1',
        'vendor.qti.hardware.radio.lpa@1.2',
        'vendor.qti.hardware.radio.qcrilhook@1.0',
        'vendor.qti.hardware.radio.qtiradio@1.0',
        'vendor.qti.hardware.radio.qtiradio@2.0',
        'vendor.qti.hardware.radio.qtiradio@2.1',
        'vendor.qti.hardware.radio.qtiradio@2.2',
        'vendor.qti.hardware.radio.qtiradio@2.3',
        'vendor.qti.hardware.radio.qtiradio@2.4',
        'vendor.qti.hardware.radio.qtiradio@2.5',
        'vendor.qti.hardware.radio.qtiradio@2.6',
        'vendor.qti.hardware.radio.uim@1.0',
        'vendor.qti.hardware.radio.uim@1.1',
        'vendor.qti.hardware.radio.uim@1.2',
        'vendor.qti.hardware.radio.uim_remote_client@1.0',
        'vendor.qti.hardware.radio.uim_remote_client@1.1',
        'vendor.qti.hardware.radio.uim_remote_client@1.2',
        'vendor.qti.hardware.radio.uim_remote_server@1.0',
        'vendor.qti.hardware.servicetracker@1.0',
        'vendor.qti.hardware.servicetracker@1.1',
        'vendor.qti.hardware.soter-V1-ndk',
        'vendor.qti.hardware.vpp@1.1',
        'vendor.qti.hardware.vpp@1.2',
        'vendor.qti.hardware.vpp@1.3',
        'vendor.qti.hardware.wigig.netperftuner@1.0',
        'vendor.qti.ims.callcapability@1.0',
        'vendor.qti.ims.callinfo@1.0',
        'vendor.qti.ims.rcsconfig@1.0',
        'vendor.qti.ims.rcsconfig@1.1',
        'vendor.qti.ims.rcsconfig@2.0',
        'vendor.qti.ims.rcsconfig@2.1',
        'vendor.qti.latency@2.0',
        'vendor.qti.latency@2.1',
        'vendor.qti.latency@2.2',
        'vendor.qti.memory.pasrmanager@1.0',
        'vendor.qti.memory.pasrmanager@1.1',
        'vendor.qti.qesdhal@1.0',
        'vendor.qti.qesdhal@1.1',
        'vendor.qti.qesdhal@1.2',
        'vendor.qti.qesdhal@1.3',
        'vendor.qti.qesdsys-V3-ndk',
        'vendor.qti.qesdsys-V4-ndk',
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
