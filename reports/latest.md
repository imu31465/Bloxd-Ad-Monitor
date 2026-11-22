# Latest ad scan

- Generated: `2026-11-22T13:35:25Z`
- Source manifest: [https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json](https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json)
- Environments: **3**
- JavaScript assets considered: **1158**
- Unique content hashes scanned or reused: **772**
- High-confidence detections: **6**
- Published filter rules: **3**

> Filter rules are emitted only for explicitly approved detector signatures in isolated lazy-loaded chunks. `main.js` is never blocked automatically. When a signature disappears, its rule is removed rather than retaining a potentially stale chunk ID.

## Current detections

| Environment | Detector | Chunk | Source file | Evidence |
|---|---|---:|---|---|
| `bloxd.io` | `aditude-instream-adapter` | `149` | `bundles/bloxd.io/chunks/js/149.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `bloxd.io` | `nitro-video-skip-overlay` | `150` | `bundles/bloxd.io/chunks/js/150.js` | `NitroSdkAdaptor`, `NitroVideoSkip`, `NitroOutstreamVideo`, `Skip ad in`, `Skip Ad`, `adStartSoPause`, `adCompleteSoResume` |
| `preprod.bloxd.io` | `aditude-instream-adapter` | `149` | `bundles/preprod.bloxd.io/chunks/js/149.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `preprod.bloxd.io` | `nitro-video-skip-overlay` | `150` | `bundles/preprod.bloxd.io/chunks/js/150.js` | `NitroSdkAdaptor`, `NitroVideoSkip`, `NitroOutstreamVideo`, `Skip ad in`, `Skip Ad`, `adStartSoPause`, `adCompleteSoResume` |
| `staging.bloxd.io` | `aditude-instream-adapter` | `149` | `bundles/staging.bloxd.io/chunks/js/149.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `staging.bloxd.io` | `nitro-video-skip-overlay` | `150` | `bundles/staging.bloxd.io/chunks/js/150.js` | `NitroSdkAdaptor`, `NitroVideoSkip`, `NitroOutstreamVideo`, `Skip ad in`, `Skip Ad`, `adStartSoPause`, `adCompleteSoResume` |

## Filter rules

- `||bloxd.io/static/js/*.150.*.chunk.js$script`
- `||preprod.bloxd.io/static/js/*.150.*.chunk.js$script`
- `||staging.bloxd.io/static/js/*.150.*.chunk.js$script`

## Changes from previous scan

No detector-location or implementation changes detected.

## Interpretation

A match means the configured signature was found in the archived JavaScript source. It does not prove the provider is selected for every player, region, or session. Blocking a detected adapter can affect the related ad flow; non-ad game logic is not intentionally targeted.
