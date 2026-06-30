# Sparse Mask Peer Validation for Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-mask-peer-validation-for-distributed-training-161484b3c6d3`
Run ID: `sparse-mask-peer-validation-for-distributed-training-161484b3c6d3-20260608T060032024137+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c7fc803dce9c

## What looked useful

Sparse masks produced mean AUC 0.9672 across 48 corruption scenarios versus 0.8549 for random signed sketches at the same k, but minimum sparse AUC fell to 0.6919 and TPR@honest-q99 to 0.0426 at low SNR. All-honest two-cluster heterogeneity caused sparse false-flag rates of 18.65% to 26.16% at 30 degrees and 64.79% to 99.95% at 60 degrees.

## Boundaries and scale limits

No real model training, no multi-node networking, no adaptive adversary, no non-IID dataset training loop, and no GPT-2-small-class baseline were run. Results are synthetic proxy evidence only.

## Claim scope

Synthetic 16-peer, 32768-dimensional CUDA simulations show that deployable leave-one-out top-k signed sparse-mask validation can detect several gross update corruptions better than random signed sketches at 0.195% to 0.781% of dense float32 communication, but it is weaker than dense peer-cosine validation and is vulnerable to honest gradient heterogeneity.

## Why it stopped

Synthetic proxy evidence is mixed: the sparse-mask mechanism works in aligned-gradient regimes but fails or becomes unsafe under low SNR and honest heterogeneity, so this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add heterogeneity-aware calibration or cluster-aware consensus and require it to preserve corruption detection while keeping all-honest non-IID false flags below 5%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneity-aware sparse mask peer validation
- Success threshold: Mean corruption AUC at least 0.94, minimum TPR@honest-q99 at least 0.50 across tested corruptions, and all-honest false-flag rate below 5% through 30-degree two-cluster heterogeneity.
- Stop condition: Stop if reducing heterogeneity false flags below 5% drops mean corruption AUC below 0.90 or minimum TPR@honest-q99 below 0.25.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-mask-peer-validation-for-distributed-training-161484b3c6d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
