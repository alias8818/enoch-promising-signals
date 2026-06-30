# Anchor-Exact KV Eviction: Deterministic Token Pinning vs Sliding Window

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-exact-kv-eviction-deterministic-token-pinning-vs-sliding-window-5d7228bfa78d`
Run ID: `anchor-exact-kv-eviction-deterministic-token-pinning-vs-sliding-window-5d7228bfa78d-20260611T181227083954+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64970e5b76f9

## What looked useful

Anchor pinning preserved exact old facts that sliding eviction dropped, with +1.0 recall delta on early-anchor retrieval and positive mixed/overflow deltas. The effect is budget- and selection-dependent: overflow recall remains low when anchors exceed pin budget, and naive first-anchor pinning can slightly hurt late-fact retention.

## Boundaries and scale limits

No real transformer, logits, latency, memory movement, RoPE behavior, or production KV-cache implementation was tested. Results support only the retention mechanism, not end-to-end model quality or serving efficiency.

## Claim scope

Synthetic, model-free retained-position probe comparing deterministic anchor pinning with a same-budget sliding KV window across early, mixed, late, and anchor-overflow retrieval distributions.

## Why it stopped

Closed as no-paper useful signal because the run produced synthetic retained-token evidence only; it is not a full validation of model behavior or serving performance.

## Recommended next action

Run a bounded deepen follow-up that implements both policies in a real attention/KV-cache path and measures answer accuracy plus latency on long-context retrieval tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV-cache anchor pinning on long-context retrieval
- Success threshold: At equal KV budget, anchor pinning improves old-fact retrieval accuracy by at least 20 percentage points over sliding window while keeping decode latency overhead below 10% on the tested model/task.
- Stop condition: Stop if anchor pinning fails to improve old-fact retrieval by 10 percentage points, causes more than 20% decode latency overhead, or implementation complexity requires non-local cache changes beyond the bounded experiment.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-eviction-deterministic-token-pinning-vs-sliding-window-5d7228bfa78d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
