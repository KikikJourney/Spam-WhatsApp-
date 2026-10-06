from urllib.parse import urlparse

def validate_target(target_url: str) -> str:
    parsed = urlparse(target_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("target must be an absolute http(s) URL")
    if parsed.username or parsed.password:
        raise ValueError("embedded credentials are not allowed")
    return target_url.rstrip("/")
