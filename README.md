# Rindoku

輪読会でのプレゼン発表資料作りを補助する CLI

## 使い方

#### プログラム概要

このプログラムは、Rindoku CLI ツールです。
指定された輪読会で使用する本のテキストを処理し、オプションで指定されたモデルとプロンプトファイルを使用して、パワーポイント形式のファイルを生成します。

#### コマンドライン引数

1. **input（必須）**

   - 説明: 輪読会で使用する本の本文テキスト
   - タイプ: 文字列
   - 例: `python main.py -i "$(cat input.txt)"`
   - 詳細: 処輪読会で使用する本のテキストを入力します。注意として、入力する文字数が長すぎると GPT の出力が終わらず、エラーが起こることがあります。

2. **-m / --model（オプション）**

   - 説明: モデル名（デフォルト: `gpt-4o-2024-08-06`）
   - タイプ: 文字列
   - デフォルト: `gpt-4o-2024-08-06`
   - 例: `python main.py -i "$(cat input.txt)" -m gpt-3`
   - 詳細: 使用するモデルの名前を指定します。指定しない場合は、デフォルトの`gpt-4o-2024-08-06`が使用されます。

3. **-p / --prompt（オプション）**
   - 説明: プロンプトファイルのパス（デフォルト: `prompt.txt`）
   - タイプ: 文字列
   - デフォルト: `prompt.txt`
   - 例: `python main.py -i "$(cat input.txt)" -p custom_prompt.txt`
   - 詳細: 使用するプロンプトファイルのパスを指定します。指定しない場合は、デフォルトの`prompt.txt`が使用されます。

3. **-s / --start（オプション）**
   - 説明: スクリプトの実行開始場所（デフォルト: `text`）
   - タイプ: 文字列
   - デフォルト: `text`
   - 例: `python main.py -i "$(cat input.txt)" -s json`
   - 詳細: スクリプトを途中から使用したい場合（例えばjsonファイルを少し変更したため、jsonファイルを入力としてプレゼン資料の生成だけ行いたいとき）、`text`, `plot`, `json`で指定できます。

#### 使用例

- デフォルトのモデルとプロンプトファイルを使用する場合

  ```sh
  python main.py -i "$(cat input.txt)"
  ```

- モデル名を指定する場合

  ```sh
  python main.py -i "$(cat input.txt)" -m gpt-3
  ```

- プロンプトファイルのパスを指定する場合
  ```sh
  python main.py -i "$(cat input.txt)" -p custom_prompt.txt
  ```

## 環境構築

Python の仮想環境（`.venv`）は、プロジェクトごとに依存関係を管理するための非常に便利なツールです。

### 1. 仮想環境の作成

まず、Python 仮想環境を作成します。

```sh
python -m venv .venv
```

これにより、現在のディレクトリに`.venv`という名前の仮想環境が作成されます。

### 2. 仮想環境の有効化

作成した仮想環境を有効化するには、以下のコマンドを実行します。

#### Windows

```sh
.venv\Scripts\activate
```

#### macOS/Linux

```sh
source .venv/bin/activate
```

これで、仮想環境が有効になります。

### 3. `requirements.txt`からパッケージをインストール

パッケージをインストールします。

```sh
pip install -r requirements.txt
```

### 4. プロンプトの作成

`prompt.txt`と`json_prompt.txt`に各プロンプト文を入力して下さい。

- `prompt.txt`
  - どのように本文を要約して、スライド形式にするかを記述するプロット用のプロンプトです。
- `json_prompt.txt`
  - プロットされた出力を json 形式に直すプロンプトです。

`prompt.txt.exmaple`と`json_prompt.txt.exmaple`を参考またはそのままコピペするとよいです。

### 5. API の追加

`.env.example`を参考にして、`.env`ファイルに `OPENAI_API_KEY`を入力してください。

### 6. 本文の入力

発表するための元の文を`input.txt`等に保存して、以下のコマンドを実行することでプレゼン資料が出力されます。

```bash
python main.py -i "$(cat input.txt)"
```

本などを使用している場合は、OCR などで抽出してください。
また著作権などの権利を侵害しない範囲内でご使用ください。

## テクニック・アドバイス

一回の実行で、大体0.10ドル程度をAPIが消費します。


同じ入力でも入力するたびに、違ったり、想定と違う間違えた出力が行われることもあるので、何度か試したり、入力内容やプロンプトを変えていくとよいです。

本文のテキストの重要な部分がスライドとして抜けている場合もあり、その時はスライドの「発表者ノート」に原文が載っているので、そこから修正していくとよいです。

またパワーポイントのデザインがそのままだと崩れているので、デザインを指定したり、スライドマスターでフォントをメイリオ等に変えるとよいです。
