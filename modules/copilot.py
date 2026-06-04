import os
from openai import OpenAI

SYSTEM_PROMPT = "あなたはMicrosoft 365研修用のCopilot風アシスタントです。短く、実務的に答えてください。"

def ask_copilot(prompt: str) -> str:
    if not prompt.strip():
        return "依頼内容を入力してください。"
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        if "要約" in prompt:
            return "【デモ応答】要点を3つに整理しました。1. 目的 2. 変更点 3. 次の対応、の順で共有すると伝わりやすくなります。"
        if "メール" in prompt:
            return "【デモ応答】件名：M365移行後の運用について\n本文：関係者各位\nM365移行後はOneDriveとSharePointを活用し、最新版ファイルを共有します。"
        return "【デモ応答】依頼内容を整理し、実務で使いやすい形に変換しました。"
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"system","content":SYSTEM_PROMPT},{"role":"user","content":prompt}],
    )
    return response.choices[0].message.content
