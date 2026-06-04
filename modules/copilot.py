import os
from openai import OpenAI

SYSTEM_PROMPT = """
あなたはMicrosoft 365移行研修用のAIアシスタントです。
回答は日本語で、職員向けに簡潔・実務的にしてください。
実在のMicrosoft Copilotそのものを名乗らず、研修用の支援AIとして振る舞ってください。
""".strip()

MOCK_RESPONSES = {
    "要約": "要点を3点に整理しました。\n1. 共有先を確認する\n2. 保存場所をOneDriveまたはSharePointに統一する\n3. Teamsで関係者に通知する",
    "メール": "件名：資料共有のご連絡\n\n関係各位\n資料を共有フォルダーに保存しました。ご確認をお願いいたします。",
    "会議": "会議前の確認事項：\n- 目的\n- 決定したい事項\n- 共有資料\n- 次のアクション",
}


def _mock_answer(prompt: str) -> str:
    for keyword, answer in MOCK_RESPONSES.items():
        if keyword in prompt:
            return answer
    return "（デモ応答）入力内容をもとに、実務で使える表現に整えました。\n\n- 目的を明確にする\n- 共有先を限定する\n- 次の作業を一文で示す"


def ask_copilot(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    if not api_key:
        return _mock_answer(prompt)

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content or _mock_answer(prompt)
    except Exception:
        return _mock_answer(prompt)
