# Contributing

Promising-signal entries are generated from deterministic Enoch control-plane fields. Do not hand-edit `data/signals.jsonl` or generated files to upgrade a result.

Before opening a PR, run:

```bash
python3 scripts/validate.py
python3 scripts/validate_public_trust_surfaces.py
git diff --check
```

Keep every entry framed as bounded local evidence, not a validated paper or public scientific claim.
