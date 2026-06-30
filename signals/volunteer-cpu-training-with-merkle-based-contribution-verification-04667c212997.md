# Volunteer CPU Training with Merkle-Based Contribution Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-cpu-training-with-merkle-based-contribution-verification-04667c212997`
Run ID: `volunteer-cpu-training-with-merkle-based-contribution-verification-04667c212997-20260611T035801898683+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c294471f56e6

## What looked useful

Merkle-sampled audits can reject broad corrupted worker updates and recover near-honest validation quality in a toy setting, but naive per-example Merkle commitments cost roughly 50x-118x the gradient computation at tested batch sizes and sparse corruption remains likely to pass small audits.

## Boundaries and scale limits

No real volunteer network, no heterogeneous hosts, no privacy or Sybil defense, no large neural model, no adaptive adversary, and no optimized cryptographic implementation. Results are bounded to a toy public-data/public-model CPU simulation.

## Claim scope

Local synthetic logistic-regression SGD with 8 simulated CPU workers, 128 examples per worker, Merkle-sum per-example gradient commitments, and random recomputation audits. The mechanism preserved training quality under broad 25% leaf-corruption attacks when audit_k=16, but naive SHA-256 Merkle construction dominated toy gradient cost.

## Why it stopped

Bounded proxy evidence is useful but not publication-grade: the sampled Merkle mechanism works against broad corruption but has high overhead in the toy workload and weak assurance against sparse cheating.

## Recommended next action

Stop this naive design as no-paper evidence; next test should compare optimized commitment or stronger aggregation-proof variants on a CPU-runnable neural baseline with explicit overhead and sparse-attack thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized contribution commitments for CPU volunteer training
- Success threshold: At least one optimized scheme achieves less than 2x end-to-end overhead versus honest baseline, validation loss within 2% of full verification under broad corruption, at least 95% detection for 25% corrupted leaves with practical audit budget, and a clear improvement over naive Merkle auditing for 1%-5% sparse corruption.
- Stop condition: Stop if all optimized schemes remain above 5x overhead on the neural CPU baseline or if sparse-corruption detection cannot improve beyond the naive sampling probability without full recomputation.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-cpu-training-with-merkle-based-contribution-verification-04667c212997`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
