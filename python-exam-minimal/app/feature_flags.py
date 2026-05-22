import hashlib
import os


def _to_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default

    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "on", "y", "t"}:
        return True
    if normalized in {"0", "false", "no", "off", "n", "f"}:
        return False
    return default


def _rollout_bucket(user_id: str) -> int:
    digest = hashlib.sha256(user_id.encode("utf-8")).hexdigest()
    return int(digest, 16) % 100


def is_next_recommender_enabled(user_id: str) -> bool:
    if not _to_bool(os.getenv("FEATURE_NEXT_RECOMMENDER"), default=False):
        return False

    raw_rollout = os.getenv("FEATURE_NEXT_RECOMMENDER_ROLLOUT", "0")
    try:
        rollout = int(raw_rollout)
    except ValueError:
        rollout = 0

    rollout = max(0, min(100, rollout))
    if rollout == 0:
        return False
    if rollout == 100:
        return True
    return _rollout_bucket(user_id) < rollout
