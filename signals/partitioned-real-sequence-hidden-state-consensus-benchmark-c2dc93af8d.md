# Partitioned Real-Sequence Hidden-State Consensus Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `partitioned-real-sequence-hidden-state-consensus-benchmark-c2dc93af8d`
Run ID: `partitioned-real-sequence-hidden-state-consensus-benchmark-c2dc93af8d-20260602T105415314065+0000`

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

- Parent run decision: Cross-Worker Hidden State Consensus: enoch://control-plane/projects/cross-worker-hidden-state-consensus-f89c619fb723/runs/cross-worker-hidden-state-consensus-f89c619fb723-20260601T062751759535+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7c1ce4c99f51

## What looked useful

Final bounded confirmation reached 92.25% mean consensus sequence accuracy across five seeds, versus 69.36% mean single-partition readout accuracy and 81.23% dense full-sequence GRU accuracy. The predefined Tier 1 threshold was met: at least 85% accuracy, at least +10 pp over single partitions, and not trailing dense control by more than 5 pp.

## Boundaries and scale limits

Evidence is limited to synthetic real-valued sequences, five seeds, 4096 training sequences per seed, one partition count, one ambiguity/dropout regime, and GRU baselines. It does not validate real-world datasets, long-context scaling, transformer architectures, or publication-grade robustness.

## Claim scope

In a small controlled synthetic real-valued sequence benchmark with four latent classes, four noisy/ambiguous partitions, and recurrent neural encoders, averaging partition-local logits recovered the shared hidden state substantially better than isolated partition readouts.

## Why it stopped

Tier 1 controlled direct evidence supports the mechanism, but the result is synthetic and small, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up with parameter-matched transformer/dense baselines, multiple partition counts and ambiguity rates, and a non-synthetic real-valued sequence dataset before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust Partition-Consensus Benchmark Against Parameter-Matched Baselines
- Success threshold: Consensus must exceed isolated partition readouts by at least 10 percentage points in most regimes and avoid trailing the best parameter-matched dense/transformer baseline by more than 5 percentage points, while preserving at least one real-data positive result.
- Stop condition: Stop as negative if the consensus advantage falls below 5 percentage points in most synthetic regimes or fails to improve over isolated partition readouts on the real-valued dataset.

## Evidence references

- Artifact root: `<local-path>/projects/partitioned-real-sequence-hidden-state-consensus-benchmark-c2dc93af8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
