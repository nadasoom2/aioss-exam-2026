from dataclasses import dataclass
from hashlib import sha256


@dataclass
class RecommendationResult:
    user_id: str
    model: str
    score: float


def old_recommender(user_id: str) -> RecommendationResult:
    digest = sha256(user_id.encode("utf-8")).digest()
    score = digest[0] / 255.0
    return RecommendationResult(user_id=user_id, model="baseline-v1", score=score)


def next_recommender(user_id: str) -> RecommendationResult:
    baseline = old_recommender(user_id)
    score = min(1.0, baseline.score + 0.12)
    return RecommendationResult(user_id=user_id, model="next-v2", score=score)
