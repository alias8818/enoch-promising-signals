# Entropy-bound gradient compression for volunteer distributed training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-bound-gradient-compression-for-volunteer-distributed-training-8ee8fe8b788b`
Run ID: `entropy-bound-gradient-compression-for-volunteer-distributed-training-8ee8fe8b788b-20260609T180813272671+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/296f2a9a06ee

## What looked useful

Entropy-bound quantization at about 1.7 observed bits/value preserved dense validation accuracy across 3 seeds with aggregate cosine 0.905 and 18.8x estimated compression, while a lower about 0.64 bits/value setting collapsed accuracy to 0.403. Baselines remained competitive, so this is a mechanism/failure-threshold signal rather than a paper result.

## Boundaries and scale limits

No real volunteer network, no straggler/dropout model, no measured entropy-coder bytes, no optimizer-state compression, no real dataset, and no GPT-2-small-class or larger model validation.

## Claim scope

Small synthetic non-IID volunteer/federated gradient simulation with 8 clients, a tiny MLP, 3 seeds, and idealized entropy bits/value accounting.

## Why it stopped

Closed as no-paper useful signal: the run directly tested toy compressed volunteer gradients and found a viable entropy-budget band plus a collapse threshold, but synthetic scale and competitive controls prevent publication-grade validation.

## Recommended next action

Run a bounded medium direct test on a small transformer or GPT-2-small-class model with real text partitions and measured entropy-coded bytes before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entropy-bound gradient compression on small-transformer non-IID text training
- Success threshold: Entropy-bound compression reaches the dense target validation loss with at least 1.5x fewer measured bytes than the best fixed/top-k compressed baseline while staying within 1% relative final validation loss of dense across at least 3 seeds.
- Stop condition: Stop if entropy-bound compression fails to beat the best fixed/top-k baseline in byte-to-loss or if accuracy/loss degrades by more than 1% relative to dense at comparable byte budgets.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-bound-gradient-compression-for-volunteer-distributed-training-8ee8fe8b788b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
