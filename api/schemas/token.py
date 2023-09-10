from fastapi import Header


def TokenRequestHeader() -> str:
    return Header(default=None, description="ウユンプニオンの認証用トークン")
