# Truncated-KV decoding check for entropy gate with old-context guard

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `truncated-kv-decoding-check-for-entropy-gate-with-old-cont-f9eeb0c9cf`
Run ID: `truncated-kv-decoding-check-for-entropy-gate-with-old-cont-f9eeb0c9cf-20260524T043231292223+0000`

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

- Parent run decision: Entropy-Gated KV Eviction for CPU Long Context: enoch://control-plane/projects/entropy-gated-kv-eviction-for-cpu-long-context-70ba78e32f49/runs/entropy-gated-kv-eviction-for-cpu-long-context-70ba78e32f49-20260524T015313102764+0000
- Parent run decision: Entropy Gate with Old-Context Coverage Guard on Real Small-Model Attention Traces: enoch://control-plane/projects/entropy-gate-with-old-context-coverage-guard-on-real-small-d5d05d35a2/runs/entropy-gate-with-old-context-coverage-guard-on-real-small-d5d05d35a2-20260524T030736264925+0000

## What looked useful

The parent attention-mass mechanism survives a direct decoding check: restoring old-context KV access changes catastrophic entropy/recency NLL deltas (~6.5-7.2) into smaller deltas (0.48-0.79 at 25% budget). The guard remains a mechanism correction, not a best policy, because stride is competitive at 25% and clearly superior at 10%.

## Boundaries and scale limits

CPU-only local run; 92 non-smoke prediction points across GPT-2-family small models; final-query attention mask only; no multi-step evolving truncated cache, serving latency, larger models, longer contexts, or task accuracy.

## Claim scope

On sampled single-step next-token predictions for distilgpt2 and gpt2, an old-context coverage guard substantially reduces NLL damage versus an unguarded entropy/recency KV truncation policy at 25% budget, but it is not consistently better than even-stride and fails against stride/heavy-hitter at 10% budget.

## Why it stopped

Moderate direct evidence is mixed: the guard fixes the entropy/recency old-context failure but does not consistently beat simple baselines on next-token NLL, especially at 10% KV budget.

## Recommended next action

Stop this branch as no-paper useful signal; the concrete next test is a bounded multi-step truncated-cache decode comparing stride, heavy-hitter, guard, and a stride+guard hybrid on the same small models.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-step truncated-cache decode for old-context guard versus stride hybrid
- Success threshold: At 10% KV budget, stride+guard or old guard must reduce mean NLL delta versus even stride by at least 0.25 with a paired 95% CI below zero, while not increasing latency by more than 15% over stride.
- Stop condition: Stop as negative if neither guard variant beats even stride on mean NLL delta at 10% budget or if multi-step truncation makes the 25% budget guard lose its advantage over unguarded entropy/recency.

## Evidence references

- Artifact root: `<local-path>/projects/truncated-kv-decoding-check-for-entropy-gate-with-old-cont-f9eeb0c9cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
