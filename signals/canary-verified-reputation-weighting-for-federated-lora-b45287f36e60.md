# Canary-verified reputation weighting for federated LoRA

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `canary-verified-reputation-weighting-for-federated-lora-b45287f36e60`
Run ID: `canary-verified-reputation-weighting-for-federated-lora-b45287f36e60-20260630T145933826069+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c910545da46

## What looked useful

Canary reputation weighting reduced poisoned aggregate weight from 0.30 to about 0.00017 in the tuned moderate-poison run and from 0.45 to about 0.00026 in the tuned high-poison run. Mean clean accuracy improved from 0.9258 FedAvg to 0.9724 canary at 30% poison and from 0.7475 FedAvg to 0.9697 canary at 45% poison. A 32-example canary set still reached 0.9661 accuracy at 45% poison in this synthetic setting.

## Boundaries and scale limits

No transformer, language-model, real dataset, secure aggregation, privacy, or adaptive-attacker validation. Seed counts are 6 to 12 and runs are under one minute each. The initial undertrained configuration showed no benefit, so the positive mechanism depends on adequate local LoRA learning signal and separable canary loss effects.

## Claim scope

Synthetic binary federated LoRA simulation with frozen linear base model, non-IID clients, non-adaptive label-flip poisoned clients, and clean private canary scoring. In tuned trainable settings, canary-scored reputation weighting sharply down-weighted poisoned LoRA deltas and improved clean held-out accuracy over FedAvg and norm-clipped averaging.

## Why it stopped

No-paper closure: this run produced synthetic mechanism evidence only, not direct federated transformer LoRA evidence or adaptive-attack robustness.

## Recommended next action

Run a bounded transformer LoRA follow-up on a small language or sequence-classification task with non-IID clients, label-flip/backdoor controls, canary scoring, and an adaptive attacker that attempts to preserve canary loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer federated LoRA canary reputation test
- Success threshold: Across at least 5 seeds, canary weighting reduces poisoned aggregate weight by >=80% versus FedAvg and improves clean validation metric by >=3 percentage points over norm-clipped averaging without degrading clean-client-only performance by more than 1 point.
- Stop condition: Stop as negative if canary weighting fails to beat norm-clipped averaging by 3 points, fails to reduce poisoned weight by 80%, or collapses under a canary-aware attacker in the bounded transformer setup.

## Evidence references

- Artifact root: `<local-path>/projects/canary-verified-reputation-weighting-for-federated-lora-b45287f36e60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
