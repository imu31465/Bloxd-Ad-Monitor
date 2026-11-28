# Latest ad scan

- Generated: `2026-11-28T11:55:30Z`
- Source manifest: [https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json](https://raw.githubusercontent.com/imu31465/Bloxd-Build-Monitor/main/.monitor-state.json)
- Environments: **3**
- JavaScript assets considered: **2132**
- Unique content hashes scanned or reused: **1421**
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

### Changed
- `{"chunk_id": "173", "detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from_sha256": "ff43f63920e18553f7fbd9e27207ece9606f8cfc2a878966217e50ab49caa8a8", "path": "bundles/bloxd.io/chunks/js/173.js", "to_sha256": "cb3f9136b4d5d43c3f0c8995e177e2845eafe9e0796bd4c84b1b7dd04882260d"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "bloxd.io", "from_sha256": "f89968a6eea88cedbcf6bf5036062c00314d7bdd43df216ae615f2b0505271ac", "path": "bundles/bloxd.io/main.js", "to_sha256": "bc4b08b5ccbabe9fe85a7d5ad70bf13571ec4686790da371554f3cec9ee0fc14"}`
- `{"chunk_id": "175", "detector_id": "aditude-instream-adapter", "environment": "bloxd.io", "from_sha256": "276203424d5c479b9045f3575960bca16802e79c4d6b12757d75870802ab4c82", "path": "bundles/bloxd.io/chunks/js/175.js", "to_sha256": "7d26caee83961ff5b64e3d632d196ed81a79af8412d483958f1e8c940340a326"}`
- `{"chunk_id": "172", "detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from_sha256": "1a6f1bde02e9ed751512a04ec7d9010aaad92b38b50329a01225cf8fb43ebd9c", "path": "bundles/bloxd.io/chunks/js/172.js", "to_sha256": "75fe19fa5d44427d98e46b258a6733d7c39f970a48df873f4a3a674661b07a46"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "bloxd.io", "from_sha256": "f89968a6eea88cedbcf6bf5036062c00314d7bdd43df216ae615f2b0505271ac", "path": "bundles/bloxd.io/main.js", "to_sha256": "bc4b08b5ccbabe9fe85a7d5ad70bf13571ec4686790da371554f3cec9ee0fc14"}`
- `{"chunk_id": "171", "detector_id": "coolmathgames-video-adapter", "environment": "bloxd.io", "from_sha256": "7062897a2cc0e5fbbf9411a00f615b2e15b376aecf6346f219104ed15e76e69f", "path": "bundles/bloxd.io/chunks/js/171.js", "to_sha256": "7d359f794230e227ecf876933451a3229902248b70e6bec74795c27c6f654ba7"}`
- `{"chunk_id": "173", "detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "ff43f63920e18553f7fbd9e27207ece9606f8cfc2a878966217e50ab49caa8a8", "path": "bundles/staging.bloxd.io/chunks/js/173.js", "to_sha256": "cb3f9136b4d5d43c3f0c8995e177e2845eafe9e0796bd4c84b1b7dd04882260d"}`
- `{"chunk_id": null, "detector_id": "adinplay-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "f89968a6eea88cedbcf6bf5036062c00314d7bdd43df216ae615f2b0505271ac", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "bc4b08b5ccbabe9fe85a7d5ad70bf13571ec4686790da371554f3cec9ee0fc14"}`
- `{"chunk_id": "175", "detector_id": "aditude-instream-adapter", "environment": "staging.bloxd.io", "from_sha256": "276203424d5c479b9045f3575960bca16802e79c4d6b12757d75870802ab4c82", "path": "bundles/staging.bloxd.io/chunks/js/175.js", "to_sha256": "7d26caee83961ff5b64e3d632d196ed81a79af8412d483958f1e8c940340a326"}`
- `{"chunk_id": "172", "detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from_sha256": "1a6f1bde02e9ed751512a04ec7d9010aaad92b38b50329a01225cf8fb43ebd9c", "path": "bundles/staging.bloxd.io/chunks/js/172.js", "to_sha256": "75fe19fa5d44427d98e46b258a6733d7c39f970a48df873f4a3a674661b07a46"}`
- `{"chunk_id": null, "detector_id": "admob-mobile-adapter", "environment": "staging.bloxd.io", "from_sha256": "f89968a6eea88cedbcf6bf5036062c00314d7bdd43df216ae615f2b0505271ac", "path": "bundles/staging.bloxd.io/main.js", "to_sha256": "bc4b08b5ccbabe9fe85a7d5ad70bf13571ec4686790da371554f3cec9ee0fc14"}`
- `{"chunk_id": "171", "detector_id": "coolmathgames-video-adapter", "environment": "staging.bloxd.io", "from_sha256": "7062897a2cc0e5fbbf9411a00f615b2e15b376aecf6346f219104ed15e76e69f", "path": "bundles/staging.bloxd.io/chunks/js/171.js", "to_sha256": "7d359f794230e227ecf876933451a3229902248b70e6bec74795c27c6f654ba7"}`

## Interpretation

A match means the configured signature was found in the archived JavaScript source. It does not prove the provider is selected for every player, region, or session. Blocking a detected adapter can affect the related ad flow; non-ad game logic is not intentionally targeted.
