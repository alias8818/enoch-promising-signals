# Anchor-Guided CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-guided-cpu-speculative-decoding-0ed3d0541802`
Run ID: `anchor-guided-cpu-speculative-decoding-0ed3d0541802-20260523T023105487758+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

Anchor gating won 27/32 regimes against tuned standard speculation, with mean +2.32%, median +2.20%, max +6.51%, and min -2.76%. Free-anchor sensitivity still reached only +7.09% max and 0/32 cases at or above 10%.

## Boundaries and scale limits

Synthetic traces only; no real LLM logits, KV-cache behavior, CPU inference kernels, natural prompts, or trained anchor predictor were measured. Main sweep used 25,000 target tokens per case and 32 regimes on one CPU worker.

## Claim scope

Dependency-free trace-level exact-decoding simulation with CPU-plausible relative costs: anchor gating often improves over tuned fixed-window speculative decoding, but only by low single digits and never by the predeclared 10% threshold across 32 tested regimes.

## Why it stopped

Proxy early falsification: the bounded simulator did not meet the 10% throughput-gain threshold over a tuned standard speculative baseline, even under free-anchor sensitivity.

## Recommended next action

Stop this generic trace-level claim as an early proxy falsification; only revisit with a real CPU inference stack if an independently measured anchor predictor can demonstrate materially stronger discrimination than the synthetic anchor used here.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU anchor predictor discrimination test
- Success threshold: At least 10% geometric-mean wall-clock tokens/s improvement over a tuned standard speculative baseline across a fixed natural-prompt suite, with no exactness regression.
- Stop condition: Stop if measured anchor discrimination plus overhead predicts less than 5% speedup before integration, or if integrated wall-clock speedup is below 10% on the fixed prompt suite.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-guided-cpu-speculative-decoding-0ed3d0541802`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
