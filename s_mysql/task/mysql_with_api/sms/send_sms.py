import json
import message


def send_message(phone, certification_number):
    data = {
        'messages': [
            {
                'to': phone,
                'from': '029302266',
                'text': f"[인증번호]\n{certification_number}"
            },
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
