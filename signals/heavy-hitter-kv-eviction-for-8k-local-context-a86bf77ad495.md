# Heavy-Hitter KV eviction for 8k local context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heavy-hitter-kv-eviction-for-8k-local-context-a86bf77ad495`
Run ID: `heavy-hitter-kv-eviction-for-8k-local-context-a86bf77ad495-20260608T151112836556+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5936459271af

## What looked useful

Pure cumulative heavy-hitter eviction is excellent for repeated anchor attention but fails recency-dominated attention, retaining only 0.0049 mass at 512 capacity versus 0.955 for local/hybrid. A half-local half-heavy-hitter hybrid preserves both constructed anchor and recency behavior, retaining 0.943 mass with 0.0292 relative MSE in the 512-capacity mixed regime.

## Boundaries and scale limits

No real decoder integration, no perplexity or task accuracy, no production paged-KV latency measurement, and no learned attention traces from real prompts. Evidence is bounded to synthetic attention regimes over 3 seeds.

## Claim scope

Synthetic 8192-token Q/K/V cache-retention simulation comparing full-context attention outputs against evicted-cache outputs for local-window, pure cumulative heavy-hitter, hybrid local+heavy-hitter, and random policies.

## Why it stopped

No-paper closure: this run is a synthetic cache-output useful signal, not direct model-quality or serving evidence. It early-falsifies pure heavy-hitter as a general replacement for local retention while supporting a bounded hybrid follow-up.

## Recommended next action

Run the hybrid local+heavy-hitter policy inside a small real decoder on fixed 8k retrieval and recency prompts, measuring perplexity/task accuracy plus latency against local-window and full-cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-decoder 8k hybrid local plus heavy-hitter KV eviction
- Success threshold: Hybrid beats local-only by at least 10 percentage points on anchor/retrieval prompts while staying within 2 percent relative degradation on recency prompts and within 10 percent latency overhead versus local-only.
- Stop condition: Stop if hybrid regresses recency prompts by more than 2 percent relative or does not beat local-only retrieval by at least 5 percentage points in the first fixed prompt suite.

## Evidence references

- Artifact root: `<local-path>/projects/heavy-hitter-kv-eviction-for-8k-local-context-a86bf77ad495`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
