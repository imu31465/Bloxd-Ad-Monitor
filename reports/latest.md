# Latest ad scan

- Generated: `2026-11-27T12:06:18Z`
- Source manifest: [https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json](https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json)
- Environments: **3**
- JavaScript assets considered: **2103**
- Unique content hashes scanned or reused: **1402**
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

### Changed
- `{"chunk_id": "166", "detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from_sha256": "c953c4afe44f056073f3d2e58b449fa8cfb8322301266ba919dc19281769c19d", "path": "bundles/bloxd.io/chunks/js/166.js", "to_sha256": "9c6e513dd5698cd55acfb05ea9bc05ac82c4abf1171e306a77f25263951fc55c"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82", "path": "bundles/bloxd.io/main.js", "to_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580"}`
- `{"chunk_id": "168", "detector_id": "aditude-instream-adapter", "environment": "bloxd.io", "from_sha256": "80710632db0bfe7912fdeb2d19c4740bb24acf285e57a852c677231db6afa0ab", "path": "bundles/bloxd.io/chunks/js/168.js", "to_sha256": "72ba201421081669ddbaf43d2e15f5b67a828729887db2b19ef26f8af7b3d237"}`
- `{"chunk_id": "165", "detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from_sha256": "4b953346702e97f649c6a4f74dbb73afe45ad91ae035b380deaaa28adf57e36d", "path": "bundles/bloxd.io/chunks/js/165.js", "to_sha256": "05535f87b1a72d6379d4bda664c543445f58a223e8b716a6b1bf730225605cd3"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82", "path": "bundles/bloxd.io/main.js", "to_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580"}`
- `{"chunk_id": "164", "detector_id": "coolmathgames-video-adapter", "environment": "bloxd.io", "from_sha256": "0db8195ccade0df6f04bc36c4000ddafa57fac9b014634836076ca24cb6b89ba", "path": "bundles/bloxd.io/chunks/js/164.js", "to_sha256": "cf8c032a8c8e86482f66e154c04a82ac7144ba4f30a43b06525741ef4e2fcf25"}`
- `{"chunk_id": "166", "detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "c953c4afe44f056073f3d2e58b449fa8cfb8322301266ba919dc19281769c19d", "path": "bundles/staging.bloxd.io/chunks/js/166.js", "to_sha256": "9c6e513dd5698cd55acfb05ea9bc05ac82c4abf1171e306a77f25263951fc55c"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580"}`
- `{"chunk_id": "168", "detector_id": "aditude-instream-adapter", "environment": "staging.bloxd.io", "from_sha256": "80710632db0bfe7912fdeb2d19c4740bb24acf285e57a852c677231db6afa0ab", "path": "bundles/staging.bloxd.io/chunks/js/168.js", "to_sha256": "72ba201421081669ddbaf43d2e15f5b67a828729887db2b19ef26f8af7b3d237"}`
- `{"chunk_id": "165", "detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from_sha256": "4b953346702e97f649c6a4f74dbb73afe45ad91ae035b380deaaa28adf57e36d", "path": "bundles/staging.bloxd.io/chunks/js/165.js", "to_sha256": "05535f87b1a72d6379d4bda664c543445f58a223e8b716a6b1bf730225605cd3"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from_sha256": "1f5157b63c4b37e0a779540df5521849bc41f050db6f7b64643a8a9d4e9f5c82", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "291cf72eda78a2ca1d0299d238787189d88202990232b3f299ddb510023c4580"}`
- `{"chunk_id": "164", "detector_id": "coolmathgames-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "0db8195ccade0df6f04bc36c4000ddafa57fac9b014634836076ca24cb6b89ba", "path": "bundles/staging.bloxd.io/chunks/js/164.js", "to_sha256": "cf8c032a8c8e86482f66e154c04a82ac7144ba4f30a43b06525741ef4e2fcf25"}`

## Interpretation

A match means the configured signature was found in the archived JavaScript source. It does not prove the provider is selected for every player, region, or session. Blocking a detected adapter can affect the related ad flow; non-ad game logic is not intentionally targeted.
