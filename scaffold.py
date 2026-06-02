from fastapi import FastAPI
from pydantic import BaseModel
import anthropic

app = FastAPI()
client = anthropic.Anthropic()


class ReceiptRequest(BaseModel):
    receipt_text: str


@app.post("/parse")
def parse_receipt(request: ReceiptRequest):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Parse this receipt and categorize each item: {request.receipt_text}"
            }
        ]
    )
    return {"result": message.content[0].text}
