# MinHash dedup threshold sweep for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-dedup-threshold-sweep-for-tiny-pretraining-a60484cd2681`
Run ID: `minhash-dedup-threshold-sweep-for-tiny-pretraining-a60484cd2681-20260609T122947300407+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/839721ff4c4c

## What looked useful

Aggressive thresholds removed most known duplicates and nearly all exact leaky validation documents, but worsened clean and held-out-topic validation loss under the fixed-update tiny-pretraining budget. High thresholds/no dedup retained leakage but achieved the best clean and held-out losses.

## Boundaries and scale limits

Toy corpus and toy model only; not a public web corpus, not GPT-2-small scale, not fixed-token/epoch controlled, and not production LSH throughput. Larger real-corpus validation could overturn the practical threshold recommendation.

## Claim scope

Controlled synthetic corpus with known near-duplicate clusters, 64-permutation MinHash over 5-token shingles, all-pairs threshold comparison, and a two-layer tiny Transformer trained for 220 fixed update steps per threshold over three seeds.

## Why it stopped

Proxy/synthetic evidence gives an early no-paper result: it does not validate MinHash threshold tuning as a tiny-pretraining loss improvement, though it does expose a useful leakage-versus-loss tradeoff.

## Recommended next action

Do not write a paper from this run; run one bounded deepen test on a small real corpus with explicit train/validation contamination labels and fixed-token as well as fixed-update controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus MinHash threshold sweep with leakage labels and compute controls
- Success threshold: A non-high threshold reduces measured validation leakage by at least 80% while clean validation loss is no worse than 1% relative to the no-dedup/high-threshold baseline in both compute-control regimes.
- Stop condition: Stop if all thresholds that reduce leakage by at least 80% worsen clean validation loss by more than 1% or if leakage labels cannot be constructed reproducibly.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-threshold-sweep-for-tiny-pretraining-a60484cd2681`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
