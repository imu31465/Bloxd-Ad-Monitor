# Latest ad scan

- Generated: `2026-11-27T03:07:55Z`
- Source manifest: [https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json](https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json)
- Environments: **3**
- JavaScript assets considered: **2103**
- Unique content hashes scanned or reused: **701**
- High-confidence detections: **18**
- Published filter rules (total): **14**
- Fixed filters: **14**
- Dynamic chunk filters: **0**

> Filter rules are emitted only for explicitly approved detector signatures in isolated lazy-loaded chunks. `main.js` is never blocked automatically. When a signature disappears, its rule is removed rather than retaining a potentially stale chunk ID.

## Current detections

| Environment | Detector | Chunk | Source file | Evidence |
|---|---|---:|---|---|
| `bloxd.io` | `adinplay-video-adapter` | `main / non-chunk` | `bundles/bloxd.io/main.js` | `AdinPlaySdkAdaptor`, `aiptag`, `adplayer`, `renderBanner` |
| `bloxd.io` | `adinplay-video-adapter` | `166` | `bundles/bloxd.io/chunks/js/166.js` | `AdinPlaySdkAdaptor`, `api.adinplay.com`, `aiptag`, `startPreRoll`, `adplayer`, `renderBanner`, `aipDisplayTag` |
| `bloxd.io` | `aditude-instream-adapter` | `168` | `bundles/bloxd.io/chunks/js/168.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `bloxd.io` | `admob-mobile-adapter` | `main / non-chunk` | `bundles/bloxd.io/main.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `bloxd.io` | `admob-mobile-adapter` | `165` | `bundles/bloxd.io/chunks/js/165.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `bloxd.io` | `coolmathgames-video-adapter` | `164` | `bundles/bloxd.io/chunks/js/164.js` | `CoolMathGamesSdkAdaptor`, `cmg-ads.js`, `cmgAdBreak`, `adBreakStart`, `adBreakComplete`, `adStartSoPause`, `adCompleteSoResume` |
| `preprod.bloxd.io` | `adinplay-video-adapter` | `main / non-chunk` | `bundles/preprod.bloxd.io/main.js` | `AdinPlaySdkAdaptor`, `aiptag`, `adplayer`, `renderBanner` |
| `preprod.bloxd.io` | `adinplay-video-adapter` | `166` | `bundles/preprod.bloxd.io/chunks/js/166.js` | `AdinPlaySdkAdaptor`, `api.adinplay.com`, `aiptag`, `startPreRoll`, `adplayer`, `renderBanner`, `aipDisplayTag` |
| `preprod.bloxd.io` | `aditude-instream-adapter` | `168` | `bundles/preprod.bloxd.io/chunks/js/168.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `preprod.bloxd.io` | `admob-mobile-adapter` | `main / non-chunk` | `bundles/preprod.bloxd.io/main.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `preprod.bloxd.io` | `admob-mobile-adapter` | `165` | `bundles/preprod.bloxd.io/chunks/js/165.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `preprod.bloxd.io` | `coolmathgames-video-adapter` | `164` | `bundles/preprod.bloxd.io/chunks/js/164.js` | `CoolMathGamesSdkAdaptor`, `cmg-ads.js`, `cmgAdBreak`, `adBreakStart`, `adBreakComplete`, `adStartSoPause`, `adCompleteSoResume` |
| `staging.bloxd.io` | `adinplay-video-adapter` | `main / non-chunk` | `bundles/staging.bloxd.io/main.js` | `AdinPlaySdkAdaptor`, `aiptag`, `adplayer`, `renderBanner` |
| `staging.bloxd.io` | `adinplay-video-adapter` | `166` | `bundles/staging.bloxd.io/chunks/js/166.js` | `AdinPlaySdkAdaptor`, `api.adinplay.com`, `aiptag`, `startPreRoll`, `adplayer`, `renderBanner`, `aipDisplayTag` |
| `staging.bloxd.io` | `aditude-instream-adapter` | `168` | `bundles/staging.bloxd.io/chunks/js/168.js` | `AditudeSdkAdaptor`, `requestInstreamPlayer`, `edge.aditude.io`, `GenericVideoWrapper` |
| `staging.bloxd.io` | `admob-mobile-adapter` | `main / non-chunk` | `bundles/staging.bloxd.io/main.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `staging.bloxd.io` | `admob-mobile-adapter` | `165` | `bundles/staging.bloxd.io/chunks/js/165.js` | `AdMobSdkAdaptor`, `ads.showRewarded`, `ads.showInterstitial`, `ads.showBanner`, `renderBanner` |
| `staging.bloxd.io` | `coolmathgames-video-adapter` | `164` | `bundles/staging.bloxd.io/chunks/js/164.js` | `CoolMathGamesSdkAdaptor`, `cmg-ads.js`, `cmgAdBreak`, `adBreakStart`, `adBreakComplete`, `adStartSoPause`, `adCompleteSoResume` |

## Filter rules

No rules were generated. The published list remains fail-open.

## Changes from previous scan

### Moved
- `{"detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from": ["165", "bundles/bloxd.io/main.js"], "to": ["166", "bundles/bloxd.io/main.js"]}`
- `{"detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from": ["164", "bundles/bloxd.io/main.js"], "to": ["165", "bundles/bloxd.io/main.js"]}`
- `{"detector_id": "coolmathgames-video-adapter", "environment": "bloxd.io", "from": ["163"], "to": ["164"]}`
- `{"detector_id": "adinplay-video-adapter", "environment": "preprod.bloxd.io", "from": ["165", "bundles/preprod.bloxd.io/main.js"], "to": ["166", "bundles/preprod.bloxd.io/main.js"]}`
- `{"detector_id": "admob-mobile-adapter", "environment": "preprod.bloxd.io", "from": ["164", "bundles/preprod.bloxd.io/main.js"], "to": ["165", "bundles/preprod.bloxd.io/main.js"]}`
- `{"detector_id": "coolmathgames-video-adapter", "environment": "preprod.bloxd.io", "from": ["163"], "to": ["164"]}`
- `{"detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from": ["165", "bundles/staging.bloxd.io/main.js"], "to": ["166", "bundles/staging.bloxd.io/main.js"]}`
- `{"detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from": ["164", "bundles/staging.bloxd.io/main.js"], "to": ["165", "bundles/staging.bloxd.io/main.js"]}`
- `{"detector_id": "coolmathgames-video-adapter", "environment": "staging.bloxd.io", "from": ["163"], "to": ["164"]}`
### Changed
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from_sha256": "ced38618233b4c0e18d8a9fca49ec2a40abbd81c126be8b9087777b7e8963d69", "path": "bundles/bloxd.io/main.js", "to_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82"}`
- `{"chunk_id": "168", "detector_id": "aditude-instream-adapter", "environment": "bloxd.io", "from_sha256": "c2354cf2e8afe6e239040291ce66c2b04a707a2505cb98c3c76a405957b023bb", "path": "bundles/bloxd.io/chunks/js/168.js", "to_sha256": "80710632db0bfe7912fdeb2d19c4740bb24acf285e57a852c677231db6afa0ab"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from_sha256": "ced38618233b4c0e18d8a9fca49ec2a40abbd81c126be8b9087777b7e8963d69", "path": "bundles/bloxd.io/main.js", "to_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "preprod.bloxd.io", "from_sha256": "c0a17c528d423c4717284de9fd99a0e60770b7dfdff10ff53725461a4acb4f92", "path": "bundles/preprod.bloxd.io/main.js", "to_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82"}`
- `{"chunk_id": "168", "detector_id": "aditude-instream-adapter", "environment": "preprod.bloxd.io", "from_sha256": "94d378571e3273b535414136283541bc7de3d9948ac2089598bc6ea3a7d28182", "path": "bundles/preprod.bloxd.io/chunks/js/168.js", "to_sha256": "80710632db0bfe7912fdeb2d19c4740bb24acf285e57a852c677231db6afa0ab"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "preprod.bloxd.io", "from_sha256": "c0a17c528d423c4717284de9fd99a0e60770b7dfdff10ff53725461a4acb4f92", "path": "bundles/preprod.bloxd.io/main.js", "to_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "ced38618233b4c0e18d8a9fca49ec2a40abbd81c126be8b9087777b7e8963d69", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82"}`
- `{"chunk_id": "168", "detector_id": "aditude-instream-adapter", "environment": "staging.bloxd.io", "from_sha256": "c2354cf2e8afe6e239040291ce66c2b04a707a2505cb98c3c76a405957b023bb", "path": "bundles/staging.bloxd.io/chunks/js/168.js", "to_sha256": "80710632db0bfe7912fdeb2d19c4740bb24acf285e57a852c677231db6afa0ab"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from_sha256": "ced38618233b4c0e18d8a9fca49ec2a40abbd81c126be8b9087777b7e8963d69", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82"}`
### Disappeared
- `{"chunk_id": "166", "detector_id": "nitro-video-skip-overlay", "environment": "bloxd.io", "note": "Detector no longer matched; generated block rule removed.", "path": "bundles/bloxd.io/chunks/js/166.js"}`
- `{"chunk_id": "166", "detector_id": "nitro-video-skip-overlay", "environment": "preprod.bloxd.io", "note": "Detector no longer matched; generated block rule removed.", "path": "bundles/preprod.bloxd.io/chunks/js/166.js"}`
- `{"chunk_id": "166", "detector_id": "nitro-video-skip-overlay", "environment": "staging.bloxd.io", "note": "Detector no longer matched; generated block rule removed.", "path": "bundles/staging.bloxd.io/chunks/js/166.js"}`

## Interpretation

A match means the configured signature was found in the archived JavaScript source. It does not prove the provider is selected for every player, region, or session. Blocking a detected adapter can affect the related ad flow; non-ad game logic is not intentionally targeted.
