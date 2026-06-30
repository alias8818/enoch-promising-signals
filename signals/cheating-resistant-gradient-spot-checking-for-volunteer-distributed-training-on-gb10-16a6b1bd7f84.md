# Cheating-Resistant Gradient Spot-Checking for Volunteer Distributed Training on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-gradient-spot-checking-for-volunteer-distributed-training-on-gb10-16a6b1bd7f84`
Run ID: `cheating-resistant-gradient-spot-checking-for-volunteer-distributed-training-on-gb10-16a6b1bd7f84-20260622T005952130803+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e0f2ec7e7459

## What looked useful

The detector had 0 false positives for honest exact gradients and overhead scaled roughly with checked microbatches: about 3.1%, 6.3%, 12.6%, and 25.4% for 1/32, 2/32, 4/32, and 8/32 checks. Sparse attacks were sampling-limited: at threshold 0.02 and 10% attacked batches, mean detection across six cheat strategies was 25%, 25%, 35%, and 50% across those check rates; at 25% attacked batches it was 20%, 45%, 75%, and 90%.

## Boundaries and scale limits

Toy synthetic classification data, one GB10 host, one small MLP, simulated workers, exact same-model recomputation, no real distributed system, no adaptive adversary, no collusion, no privacy or commitment layer, and no end-to-end training convergence measurement.

## Claim scope

Exact random server recomputation of assigned microbatch gradients detects non-adaptive scaled, stale, noisy, zero, and sign-flipped gradient tampering in a small CUDA/PyTorch MLP probe when at least one corrupted microbatch is sampled.

## Why it stopped

No-paper closure: this run produced a useful local mechanism signal but only on toy synthetic gradients, and the sparse-attack sampling limit prevents a broad cheating-resistant distributed-training claim.

## Recommended next action

Run a bounded multi-round simulated volunteer training follow-up that measures cumulative sparse-attack detection and convergence impact versus no-check and full-check controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cumulative Multi-Round Gradient Spot-Check Detection Under Sparse Volunteer Cheating
- Success threshold: At no more than 10% recomputation overhead, detect at least 95% of persistent workers that corrupt 5-10% of assigned microbatches within a bounded number of rounds while keeping final validation quality within 2% of the honest baseline.
- Stop condition: Stop if cumulative detection remains below 80% at 10% overhead or if model quality degrades by more than 5% relative to the honest baseline under the spot-check policy.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-gradient-spot-checking-for-volunteer-distributed-training-on-gb10-16a6b1bd7f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
