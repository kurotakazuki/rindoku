# Rindoku

輪読会でのプレゼン発表資料作りを補助する CLI

## 使い方

#### プログラム概要

このプログラムは、Rindoku CLI ツールです。
指定された輪読会で使用する本のテキストを処理し、オプションで指定されたモデルとプロンプトファイルを使用して出力を生成します。

#### コマンドライン引数

1. **input（必須）**

   - 説明: 輪読会で使用する本のテキスト
   - タイプ: 文字列
   - 例: `python main.py -i "$(cat input.txt)"`
   - 詳細: 処輪読会で使用する本のテキストを入力します。

2. **-m / --model（オプション）**

   - 説明: モデル名（デフォルト: `gpt-4o`）
   - タイプ: 文字列
   - デフォルト: `gpt-4o`
   - 例: `python main.py -i "$(cat input.txt)" -m gpt-3`
   - 詳細: 使用するモデルの名前を指定します。指定しない場合は、デフォルトの`gpt-4o`が使用されます。

3. **-p / --prompt（オプション）**
   - 説明: プロンプトファイルのパス（デフォルト: `prompt.txt`）
   - タイプ: 文字列
   - デフォルト: `prompt.txt`
   - 例: `python main.py -i "$(cat input.txt)" -p custom_prompt.txt`
   - 詳細: 使用するプロンプトファイルのパスを指定します。指定しない場合は、デフォルトの`prompt.txt`が使用されます。

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
