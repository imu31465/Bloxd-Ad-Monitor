# Bloxd Ad Monitor

**独立して動作する、Bloxdの広告関連JavaScriptモジュール追跡・フィルター生成プロジェクト。**

Bloxdの新しいビルドを定期確認し、JavaScriptチャンクの中身から既知の広告アダプターを検出します。検出されたチャンクIDが変わった場合は追跡結果とuBlock Origin互換のフィルターリストを自動更新します。

- Repository: <https://github.com/imu31465/Bloxd-Ad-Monitor>
- Data source: <https://github.com/imu31465/Bloxd-Build-Monitor>（読み取り専用。変更・トークン・Webhook連携は不要）
- Latest report: [`reports/latest.md`](reports/latest.md)
- Latest machine-readable report: [`reports/latest.json`](reports/latest.json)
- Generated combined filter list: [`filters/bloxd-video-adapters.txt`](filters/bloxd-video-adapters.txt)
- Fixed Bloxd rules: [`config/static-filters.txt`](config/static-filters.txt)

## uBlock Origin Liteでの利用

uBlock Origin Liteの外部フィルターリスト購読に対応した版（2026.621.1813以降）では、ダッシュボードの **Filter lists** を開き、下部の **Add filter list...** から次のURLを登録します。

```text
https://raw.githubusercontent.com/imu31465/Bloxd-Ad-Monitor/main/filters/bloxd-video-adapters.txt
```

このURL **1つ** に、以前使っていた固定のドメインブロック・要素非表示・対応スクリプトレットと、Nitroなどの広告チャンクを追跡して生成する動的ルールをまとめています。固定ルールは `config/static-filters.txt`、チャンクルールはビルド解析から自動生成されます。チャンク番号が変われば次回スキャンで動的ルールだけが更新されます。

要素非表示・スクリプトレットも適用するには、ブラウザーの拡張機能詳細でuBlock Origin Liteの **Allow User Scripts** を有効にし、Bloxdでのフィルタリングモードを **Optimal** または **Complete** にしてください。Basicではネットワークブロックのみが適用されます。外部リストから読み込めるスクリプトレットはuBO Liteに同梱されたものに限られます。

以前の `no-document-write` ルールは、現行の公式uBOスクリプトレット一覧に存在を確認できなかったため、統合リストには含めていません。リストの取得・再取得タイミングはuBlock Origin Liteとブラウザー側の管理に依存するため、GitHub上の生成結果とブラウザーに反映済みのルールが一時的にずれる場合があります。

## 仕組み

1. GitHub Actionsが5分ごとにBuild Monitorの`.monitor-state.json`を読み取ります。手動実行も可能です。
2. マニフェストに列挙されたJSファイルだけを確認します。CSSやWASMは取得しません。
3. 各ファイルのSHA-256を照合してから、設定済みの広告シグネチャを検査します。
4. 同じSHA-256のファイルは`.state/scan-cache.json`の検出結果を再利用し、再ダウンロードしません。
5. 現在の検出場所と前回の検出場所を比較し、チャンクIDの移動・コード変更・検出消失をレポートします。
6. 高信頼かつ明示的に許可された検出だけからフィルターを生成し、レポートとともにコミットします。

Build Monitorは読み取り専用のデータ供給元です。Build Monitor側のコード、ワークフロー、データ形式を変更する必要はありません。

## 安全側の公開ルール

- `main.js`は自動ブロックしません。ゲーム本体の大きなバンドルを広告検出だけで止めることを避けます。
- ファイル名やチャンク番号だけでは広告と判定しません。コード内の複数の特徴が同時に確認された場合だけ検出します。
- 現在の初期ルールは、Nitroの動画スキップUI・ゲーム一時停止制御・アダプター識別子が同一チャンク内で確認された場合に限って生成します。
- Aditudeのインストリームアダプターは追跡しますが、タイマー付きスキップ画面との関連が確認できていないため自動ブロックしません。
- 取得に失敗したファイル、SHA-256不一致、部分的なスキャンがあれば処理全体を失敗させます。古い結果を最新の結果として公開しません。
- 検出シグネチャが消えた場合は古いチャンク番号のルールを残さず、レポートに「検出消失」として記録します。これは誤った別機能をブロックし続けないためのfail-open動作です。

## ローカル実行

Python 3.11以降、追加パッケージ不要です。

```bash
python -m bloxd_ad_monitor
```

オプション:

```bash
python -m bloxd_ad_monitor --manifest-url URL --raw-base-url URL
python -m bloxd_ad_monitor --manifest-file ./fixtures/manifest.json --source-root ./fixtures/source
python -m unittest discover -s tests -v
```

## 検出シグネチャの追加・修正

[`config/detectors.json`](config/detectors.json)を編集します。各検出器の`required_groups`はAND条件のグループ配列で、各グループ内はOR条件です。たとえば4グループすべてに少なくとも1つの特徴文字列が必要です。

`publish_filter`は初期値を`false`にしてください。実際のバンドルで複数ビルドにわたり確認し、独立した広告専用チャンクであると判断できた検出器だけ`true`にします。設定変更時はシグネチャのフィンガープリントが変わるため、過去の検出キャッシュは自動的に無効化されます。

## 制限

- コード内のシグネチャ検出であり、実行時の広告プロバイダー選択や地域・アカウントごとの配信を保証するものではありません。
- 広告事業者がコードの識別子や実装を変更した場合、検出器の見直しが必要です。
- uBlock Origin Liteのフィルター対応範囲や更新タイミングはブラウザー側に依存します。リスト更新直後に即時反映されるとは限りません。
- フィルターは広告アダプターのチャンク通信を止めます。広告周辺の挙動が変わる可能性があるため、最新レポートとテスト結果を確認して利用してください。
- Nitroの検出対象チャンクには15秒スキップUIだけでなく、Nitroのバナー描画処理（`renderBanner`）も含まれています。生成ルールはチャンク全体をブロックするため、カウントダウンだけでなくNitro経由のバナー等も動作しなくなる可能性があります。

## ライセンス

MIT. See [LICENSE](LICENSE).
