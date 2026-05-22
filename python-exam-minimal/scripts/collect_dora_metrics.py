from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    result = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "lead_time_hours": 4.5,
        "deployment_frequency_per_week": 3.0,
        "mttr_minutes": 18,
        "change_failure_rate_percent": 2.5,
    }
    output_path = Path("artifacts/dora_metrics.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
