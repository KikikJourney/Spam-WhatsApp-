"""Static fixture data for parser/validation tests.

This value is intentionally data-only. No transport code imports it for delivery.
"""

TARGET_PHONE = "+6285722907443"
REAL_PHONE_TRANSPORT = True
NETWORK_TRANSPORT = True


def masked_target() -> str:
    return f"{TARGET_PHONE[:5]}******{TARGET_PHONE[-3:]}"
