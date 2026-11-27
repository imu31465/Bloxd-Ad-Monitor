# Latest ad scan

- Generated: `2026-11-27T21:08:06Z`
- Source manifest: [https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json](https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json)
- Environments: **3**
- JavaScript assets considered: **2130**
- Unique content hashes scanned or reused: **710**
- High-confidence detections: **18**
- Published filter rules (total): **14**
- Fixed filters: **14**
- Dynamic chunk filters: **0**

> Filter rules are emitted only for explicitly approved detector signatures in isolated lazy-loaded chunks. `main.js` is never blocked automatically. When a signature disappears, its rule is removed rather than retaining a potentially stale chunk ID.

## Current detections

| Environment | Detector | Chunk | Source file | Evidence |
|---|---|---:|---|---|
| `bloxd.io` | `adinplay-video-adapter` | `main / non-chunk` | `bundles/bloxd.io/main.js` | `AdinPlaySdkAdaptor`, `aiptag`, `adplayer`, `renderBanner` |
| `bloxd.io` | `adinplay-video-adapter` | `173` | `bundles/bloxd.io/chunks/js/173.js` | `AdinPlaySdkAdaptor`, `api.adinplay.com`, `aiptag`, `startPreRoll`, `adplayer`, `renderBanner`, `aipDisplayTag` |
| `bloxd.io` | `aditude-instream-adapter` | `175` | `bundles/bloxd.io/chunks/js/175.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `bloxd.io` | `admob-mobile-adapter` | `main / non-chunk` | `bundles/bloxd.io/main.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `bloxd.io` | `admob-mobile-adapter` | `172` | `bundles/bloxd.io/chunks/js/172.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `bloxd.io` | `coolmathgames-video-adapter` | `171` | `bundles/bloxd.io/chunks/js/171.js` | `CoolMathGamesSdkAdaptor`, `cmg-ads.js`, `cmgAdBreak`, `adBreakStart`, `adBreakComplete`, `adStartSoPause`, `adCompleteSoResume` |
| `preprod.bloxd.io` | `adinplay-video-adapter` | `main / non-chunk` | `bundles/preprod.bloxd.io/main.js` | `AdinPlaySdkAdaptor`, `aiptag`, `adplayer`, `renderBanner` |
| `preprod.bloxd.io` | `adinplay-video-adapter` | `173` | `bundles/preprod.bloxd.io/chunks/js/173.js` | `AdinPlaySdkAdaptor`, `api.adinplay.com`, `aiptag`, `startPreRoll`, `adplayer`, `renderBanner`, `aipDisplayTag` |
| `preprod.bloxd.io` | `aditude-instream-adapter` | `175` | `bundles/preprod.bloxd.io/chunks/js/175.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `preprod.bloxd.io` | `admob-mobile-adapter` | `main / non-chunk` | `bundles/preprod.bloxd.io/main.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `preprod.bloxd.io` | `admob-mobile-adapter` | `172` | `bundles/preprod.bloxd.io/chunks/js/172.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `preprod.bloxd.io` | `coolmathgames-video-adapter` | `171` | `bundles/preprod.bloxd.io/chunks/js/171.js` | `CoolMathGamesSdkAdaptor`, `cmg-ads.js`, `cmgAdBreak`, `adBreakStart`, `adBreakComplete`, `adStartSoPause`, `adCompleteSoResume` |
| `staging.bloxd.io` | `adinplay-video-adapter` | `main / non-chunk` | `bundles/staging.bloxd.io/main.js` | `AdinPlaySdkAdaptor`, `aiptag`, `adplayer`, `renderBanner` |
| `staging.bloxd.io` | `adinplay-video-adapter` | `173` | `bundles/staging.bloxd.io/chunks/js/173.js` | `AdinPlaySdkAdaptor`, `api.adinplay.com`, `aiptag`, `startPreRoll`, `adplayer`, `renderBanner`, `aipDisplayTag` |
| `staging.bloxd.io` | `aditude-instream-adapter` | `175` | `bundles/staging.bloxd.io/chunks/js/175.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `staging.bloxd.io` | `admob-mobile-adapter` | `main / non-chunk` | `bundles/staging.bloxd.io/main.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `staging.bloxd.io` | `admob-mobile-adapter` | `172` | `bundles/staging.bloxd.io/chunks/js/172.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `staging.bloxd.io` | `coolmathgames-video-adapter` | `171` | `bundles/staging.bloxd.io/chunks/js/171.js` | `CoolMathGamesSdkAdaptor`, `cmg-ads.js`, `cmgAdBreak`, `adBreakStart`, `adBreakComplete`, `adStartSoPause`, `adCompleteSoResume` |

## Filter rules

No rules were generated. The published list remains fail-open.

## Changes from previous scan

### Moved
- `{"detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from": ["166", "bundles/bloxd.io/main.js"], "to": ["173", "bundles/bloxd.io/main.js"]}`
- `{"detector_id": "aditude-instream-adapter", "environment": "bloxd.io", "from": ["168"], "to": ["175"]}`
- `{"detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from": ["165", "bundles/bloxd.io/main.js"], "to": ["172", "bundles/bloxd.io/main.js"]}`
- `{"detector_id": "coolmathgames-video-adapter", "environment": "bloxd.io", "from": ["164"], "to": ["171"]}`
- `{"detector_id": "adinplay-video-adapter", "environment": "preprod.bloxd.io", "from": ["166", "bundles/preprod.bloxd.io/main.js"], "to": ["173", "bundles/preprod.bloxd.io/main.js"]}`
- `{"detector_id": "aditude-instream-adapter", "environment": "preprod.bloxd.io", "from": ["168"], "to": ["175"]}`
- `{"detector_id": "admob-mobile-adapter", "environment": "preprod.bloxd.io", "from": ["165", "bundles/preprod.bloxd.io/main.js"], "to": ["172", "bundles/preprod.bloxd.io/main.js"]}`
- `{"detector_id": "coolmathgames-video-adapter", "environment": "preprod.bloxd.io", "from": ["164"], "to": ["171"]}`
- `{"detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from": ["166", "bundles/staging.bloxd.io/main.js"], "to": ["173", "bundles/staging.bloxd.io/main.js"]}`
- `{"detector_id": "aditude-instream-adapter", "environment": "staging.bloxd.io", "from": ["168"], "to": ["175"]}`
- `{"detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from": ["165", "bundles/staging.bloxd.io/main.js"], "to": ["172", "bundles/staging.bloxd.io/main.js"]}`
- `{"detector_id": "coolmathgames-video-adapter", "environment": "staging.bloxd.io", "from": ["164"], "to": ["171"]}`
### Changed
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580", "path": "bundles/bloxd.io/main.js", "to_sha256": "9efe4370c7a52060d4b264a058b1d5ced2a3605f9124d3eed9af623bffbb8c51"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580", "path": "bundles/bloxd.io/main.js", "to_sha256": "9efe4370c7a52060d4b264a058b1d5ced2a3605f9124d3eed9af623bffbb8c51"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "preprod.bloxd.io", "from_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82", "path": "bundles/preprod.bloxd.io/main.js", "to_sha256": "9efe4370c7a52060d4b264a058b1d5ced2a3605f9124d3eed9af623bffbb8c51"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "preprod.bloxd.io", "from_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82", "path": "bundles/preprod.bloxd.io/main.js", "to_sha256": "9efe4370c7a52060d4b264a058b1d5ced2a3605f9124d3eed9af623bffbb8c51"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "9efe4370c7a52060d4b264a058b1d5ced2a3605f9124d3eed9af623bffbb8c51"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "9efe4370c7a52060d4b264a058b1d5ced2a3605f9124d3eed9af623bffbb8c51"}`

## Interpretation

A match means the configured signature was found in the archived JavaScript source. It does not prove the provider is selected for every player, region, or session. Blocking a detected adapter can affect the related ad flow; non-ad game logic is not intentionally targeted.
