from fastapi import Request


async def verify_token(request: Request, call_next):
    print("hoge")
    response = await call_next(request)
    print("fuga")
    return response
