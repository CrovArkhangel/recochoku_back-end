import whisper


def transcribe_audio(file_path):
    # Whisperモデルをロード
    model = whisper.load_model("large")

    # 指定された音声ファイルを文字起こし
    result = model.transcribe(file_path, verbose=True, language='ja')

    # 結果からテキストを取得
    text = result['text']

    return text


# usage
# file_name = "test1.m4a"
# transcribed_text = transcribe_audio(file_name)
# print(transcribed_text)
