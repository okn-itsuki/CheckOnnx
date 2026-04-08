import onnxruntime as ort
import sys

# コマンドライン引数からパスを取得
if len(sys.argv) < 2:
    print("使用法: python CheckOnnx.py [ONNXファイルのパス]")
    sys.exit(1)

model_path = sys.argv[1]

try:
    session = ort.InferenceSession(model_path)

    print(f"--- Model: {model_path} ---")

    print("\n[Inputs]")
    for node in session.get_inputs():
        print(f"  Name: {node.name}\n Shape: {node.shape}\n Type: {node.type}")

    print("\n[Outputs]")
    for node in session.get_outputs():
        print(f"  Name: {node.name}\n Shape: {node.shape}\n Type: {node.type}")

except Exception as e:
    print(f"エラーが発生しました: {e}")