from fastapi import Header


def TokenRequestHeader():
    return Header(default=None, description="ウユンプニオンの認証用トークン")
