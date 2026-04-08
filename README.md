onnx model の tensor の型をローカルで簡単に調べるために作りました。

## 1. 前提条件
```
- OS: Windows / Linux / macOS
- Python: 3.8以上（※3.13でも動作確認済み）
- pip
- onnxruntime
```
## 2. セットアップ
### 2.1 プロジェクトディレクトリ作成
```sh
mkdir OnnxIoCheck
cd OnnxIoCheck
```
### 2.2 仮想環境作成
```sh
python -m venv venv
```
### 2.3 仮想環境の有効化
* Windows（Git Bash）
```sh
source venv/Scripts/activate
```
* Windows（PowerShell）
```sh
venv\Scripts\Activate.ps1
```
* Linux / macOS
```sh
source venv/bin/activate
```
### 2.4 必要パッケージのインストール
```sh
pip install onnxruntime onnx
```
## 3. 実行方法
```sh
python CheckOnnx.py "モデルのパス"
# 例
python CheckOnnx.py "C:\Users\yourname\model.onnx"
```
# 4. 最短手順
```sh
python -m venv venv
source venv/Scripts/activate
pip install onnxruntime onnx
python CheckOnnx.py model.onnx
```
