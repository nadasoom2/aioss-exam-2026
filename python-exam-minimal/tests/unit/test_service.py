# TODO: 단위 테스트 최소 3개를 작성하세요.
# 예시 주제(정답 아님):
# - old_recommender model 검증
# - next_recommender model 검증
# - next_recommender 점수 정책 검증

from app.service import next_recommender, old_recommender


def test_old_recommender_uses_baseline_model() -> None:
    result = old_recommender("user-001")

    assert result.user_id == "user-001"
    assert result.model == "baseline-v1"
    assert 0.0 <= result.score <= 1.0


def test_next_recommender_uses_next_model() -> None:
    result = next_recommender("user-002")

    assert result.user_id == "user-002"
    assert result.model == "next-v2"
    assert 0.0 <= result.score <= 1.0


def test_next_recommender_score_is_not_worse_than_baseline() -> None:
    baseline = old_recommender("user-003")
    next_result = next_recommender("user-003")

    assert next_result.score >= baseline.score
