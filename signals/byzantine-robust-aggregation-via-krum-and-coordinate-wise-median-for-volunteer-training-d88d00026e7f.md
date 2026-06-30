# Byzantine-Robust Aggregation via Krum and Coordinate-wise Median for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `byzantine-robust-aggregation-via-krum-and-coordinate-wise-median-for-volunteer-training-d88d00026e7f`
Run ID: `byzantine-robust-aggregation-via-krum-and-coordinate-wise-median-for-volunteer-training-d88d00026e7f-20260620T112514596771+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/35b446046754

## What looked useful

Coordinate-wise median was the best robust default in this bounded proxy. Krum was attack-resistant but less efficient/aligned because it selected a single client update. Plain mean collapsed under scaled sign-flip Byzantine updates.

## Boundaries and scale limits

No deep-network benchmark, real volunteer trace, partial participation, asynchronous behavior, secure aggregation, adaptive adversary, privacy noise, compression, or production systems validation was run.

## Claim scope

Small synthetic federated logistic-regression proxy with 25 clients, 6 Byzantine clients, IID and label-skewed non-IID client data, and signflip/Gaussian/label-flip attacks. Coordinate-wise median preserved near-clean accuracy and high clean-update alignment; Krum avoided Byzantine selections but had lower alignment and modestly lower accuracy.

## Why it stopped

Synthetic CPU-only proxy produced useful mechanism evidence but not publication-grade direct validation for volunteer training.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded PyTorch image-classification follow-up with partial participation, adaptive attacks, and communication-matched convergence curves.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust aggregation under partial-participation neural federated learning
- Success threshold: Median beats mean and Krum by at least 2 percentage points final accuracy or reaches the same accuracy in at least 25% fewer communication rounds under two or more attacks without more than 1 point no-attack accuracy loss.
- Stop condition: Stop as negative if median does not outperform both mean and Krum under any adaptive attack or if its no-attack convergence cost exceeds 5 accuracy points at the matched round budget.

## Evidence references

- Artifact root: `<local-path>/projects/byzantine-robust-aggregation-via-krum-and-coordinate-wise-median-for-volunteer-training-d88d0002`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
