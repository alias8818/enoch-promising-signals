# Honeypot Gradient Verification for Volunteer Aggregation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `honeypot-gradient-verification-for-volunteer-aggregation-3dae29c94eda`
Run ID: `honeypot-gradient-verification-for-volunteer-aggregation-3dae29c94eda-20260628T013527193642+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f232d869c4a5

## What looked useful

Honeypot gating perfectly rejected non-adaptive broad gradient corruption in the synthetic test and reduced relative error to the clean-honest level, but it completely failed when attackers could distinguish honeypots and return correct honeypot gradients while corrupting task gradients.

## Boundaries and scale limits

No real model training, no real volunteer hardware, no cryptographic or protocol-level hiding of honeypot work, and no full adaptive adversary beyond the direct ability to answer honeypots honestly while poisoning task gradients.

## Claim scope

Synthetic volunteer gradient aggregation with 64 workers, 25% malicious workers, 4096-dimensional task gradients, 128-dimensional server-known honeypot gradients, and six attack/adaptivity scenarios over 500 trials each.

## Why it stopped

No-paper useful signal: synthetic evidence supports the canary mechanism only for non-adaptive corruption and early-falsifies standalone honeypot verification against distinguishable adaptive attacks; this is not full validation.

## Recommended next action

Run a bounded deepen test where honeypot and task gradients are embedded indistinguishably in a toy training workload, then measure adaptive attacker detection and task-loss impact.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Indistinguishable Honeypot Gradients in a Toy Training Pipeline
- Success threshold: At 25% malicious volunteers, honeypot-gated aggregation should detect at least 80% of adaptive malicious submissions with no more than 5% honest false positives and achieve lower task loss or gradient relative error than coordinate median and trimmed mean across at least three attack types.
- Stop condition: Stop if adaptive attackers can still pass honeypots with detection TPR below 50% or if honest false positives exceed 10% under calibrated noise, because the mechanism would require stronger protocol assumptions.

## Evidence references

- Artifact root: `<local-path>/projects/honeypot-gradient-verification-for-volunteer-aggregation-3dae29c94eda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
