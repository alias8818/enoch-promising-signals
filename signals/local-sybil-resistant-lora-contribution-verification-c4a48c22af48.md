# Local Sybil-Resistant LoRA Contribution Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-sybil-resistant-lora-contribution-verification-c4a48c22af48`
Run ID: `local-sybil-resistant-lora-contribution-verification-c4a48c22af48-20260610T185438633867+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58369bbbc25c

## What looked useful

Per-submission validation credit let cloned Sybils capture 53.4% attacker share with 8 identities and 69.8% with 16 identities. Cosine clustering capped exact clones near one honest contributor but cannot link low-cosine coordinate shards. Greedy marginal scoring removed scaled-clone and coordinate-shard credit in the main run, but clone behavior was unstable and synthetic-only.

## Boundaries and scale limits

Tested only on small synthetic frozen-linear tasks with rank-4 deltas, 8 honest clients, and up to 16 Sybil identities. Not tested on transformer LoRA, real data heterogeneity, adaptive adversarial search, collusion among multiple real actors, or external identity/stake systems.

## Claim scope

Synthetic linear LoRA-analogue evidence shows independent local validation scoring is Sybil-vulnerable; cosine clustering mitigates identical-direction clones but is not a complete local-only Sybil defense; greedy marginal validation credit is a plausible bounded mitigation but not paper-ready.

## Why it stopped

No-paper useful signal from a bounded synthetic probe; result is not a full validation or publication-grade transformer LoRA claim.

## Recommended next action

Run a bounded GPT-2-small-class LoRA verification follow-up comparing independent, cosine-clustered, and greedy marginal credit under adaptive clone, scaled-clone, and low-cosine shard attacks with honest false-rejection controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2 LoRA Marginal-Credit Verification Under Adaptive Sybil Splits
- Success threshold: Greedy marginal credit keeps attacker_vs_best_honest <= 1.25 for all tested split attacks while preserving at least 80% of honest contributors with positive standalone utility, and independent or cosine-only baselines fail at least one attack by exceeding attacker_vs_best_honest >= 2.0.
- Stop condition: Stop if greedy marginal credit exceeds attacker_vs_best_honest 2.0 on any adaptive split attack, or if honest false rejection exceeds 50%, because the bounded mitigation would not be viable.

## Evidence references

- Artifact root: `<local-path>/projects/local-sybil-resistant-lora-contribution-verification-c4a48c22af48`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
