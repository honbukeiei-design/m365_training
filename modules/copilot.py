import os

try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None


def ask_copilot(prompt: str) -> str:
    """Optional AI demo. Falls back to a deterministic response when no API key is set."""
    if not prompt.strip():
        return "まずは、やりたい作業を1文で入力してください。"
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and OpenAI:
        try:
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたはMicrosoft 365研修用のアシスタントです。操作手順を短く説明してください。"},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content or "回答を生成できませんでした。"
        except Exception:
            pass
    return (
        "研修用デモ応答：\n\n"
        f"依頼内容「{prompt}」に対して、まず目的を1行で整理し、次に作業手順を3つに分けます。\n"
        "1. 対象ファイルを開く\n2. 必要な箇所を編集・共有する\n3. 保存状態と共有先を確認する"
    )
