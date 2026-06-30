# Verified Volunteer Draft Models for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verified-volunteer-draft-models-for-speculative-decoding-4b8e8d1e6da2`
Run ID: `verified-volunteer-draft-models-for-speculative-decoding-4b8e8d1e6da2-20260524T183733845200+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9035c693eab8

## What looked useful

Across 640 simulated runs, exact target output was preserved in every scenario, including adversarial and stale volunteers. Reputation selection reached 2.088x mean proxy speedup in a mixed pool versus 0.844x for fastest-only selection when the fastest volunteer was adversarial. Low-quality pools gave only 1.134x, showing that verified volunteers are safe in this model but not automatically useful.

## Boundaries and scale limits

No real LLM target/draft serving was run. Results are synthetic trace and latency-model evidence only; they do not validate GPU verifier timing, KV-cache behavior, prompt-dependent acceptance, real network latency, privacy/security economics, or production tail latency.

## Claim scope

Trace-level simulator evidence shows that target verification preserves exact output under untrusted volunteer draft proposals, and that reputation-gated volunteer selection can improve proxy throughput when at least one volunteer has sufficiently high accepted-token rate and low latency.

## Why it stopped

Proxy-only useful signal, not full validation: synthetic traces support safety and conditional throughput but do not provide direct model-serving evidence for a paper.

## Recommended next action

Stop this proxy run; next useful action is a bounded real-LLM follow-up with a small target/draft pair, adversarial/stale volunteer processes, and measured tokens/sec plus p50/p95 latency against no-speculation and trusted-local-drafter baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-LLM Verified Volunteer Speculative Decoding
- Success threshold: Exact output equality on all evaluated prompts and at least 1.2x mean tokens/sec over target-only decoding with no p95 latency regression greater than 10% in the mixed volunteer pool.
- Stop condition: Stop if exact-output equality fails once, or if the best mixed-pool configuration remains below 1.05x mean tokens/sec after tuning draft length and selector exploration within the bounded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/verified-volunteer-draft-models-for-speculative-decoding-4b8e8d1e6da2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
