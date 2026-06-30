# Robust Aggregation Defense Against Gradient Cheaters in Volunteer CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `robust-aggregation-defense-against-gradient-cheaters-in-volunteer-cpu-training-69a66d7cf36a`
Run ID: `robust-aggregation-defense-against-gradient-cheaters-in-volunteer-cpu-training-69a66d7cf36a-20260620T235631993193+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/871b7fc1a29f

## What looked useful

Across 1,200 scored cases, coordinate median and oracle-f trimmed mean each reached 0.900 success rate with mean cosine to the clean honest aggregate of 0.936 and 0.932. Plain mean reached 0.500, norm-clipped mean 0.858, and Krum 0.000 under the strict update-fidelity success criterion. Krum still often reduced held-out loss but selected updates too far from the clean aggregate in this non-IID setting.

## Boundaries and scale limits

Synthetic one-step logistic-regression gradients only; no real LLM/pretraining gradients, no multi-round convergence, no unknown-f estimation, no multi-node volunteer runtime, and no adaptive coordinator-aware attacker.

## Claim scope

In a bounded synthetic logistic-regression volunteer-gradient simulation with 31 non-IID clients, coordinate median and oracle-f trimmed mean preserved useful honest-update direction under simple gradient-cheating attacks better than plain mean, norm clipping, or Krum.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but is not direct/full validation for volunteer CPU LLM training.

## Recommended next action

Run a bounded direct-gradient follow-up on a tiny PyTorch transformer or GPT-2-small-class replay with unknown cheater fraction and multi-round convergence before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer direct-gradient robust aggregation replay under adaptive cheaters
- Success threshold: Robust aggregator improves held-out loss in at least 90% of attacked rounds and stays within 10% of clean-run final held-out loss while FedAvg fails under at least one attack family.
- Stop condition: Stop as negative if robust aggregation does not outperform FedAvg on held-out loss or clean-update cosine in two independent seeds, or if non-IID honest variance dominates all attack effects.

## Evidence references

- Artifact root: `<local-path>/projects/robust-aggregation-defense-against-gradient-cheaters-in-volunteer-cpu-training-69a66d7cf36a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
