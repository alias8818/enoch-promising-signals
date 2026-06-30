# Merkle-Gradient Byzantine Detection Toy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-gradient-byzantine-detection-toy-bf85e323b55d`
Run ID: `merkle-gradient-byzantine-detection-toy-bf85e323b55d-20260523T215600100157+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4550ade894df

## What looked useful

Merkle-gradient verification had 1.000 recall for post-commit tamper/equivocation and 0.000 recall for consistently committed semantic Byzantine gradients across sign-flip, orthogonal, and small-bias attacks. The mechanism is integrity checking, not standalone Byzantine-gradient detection.

## Boundaries and scale limits

Synthetic CPU-only toy: 200 trials, 32 workers, 1024-dimensional gradients, 25% Byzantine workers, three hand-coded attacks. No real model training, network stack, partial chunk sampling, colluding aggregators, or large-scale federated deployment was tested.

## Claim scope

Plain Merkle commitments over gradient chunks detect post-commit gradient mutation/equivocation in a synthetic distributed-gradient toy, but do not detect workers that honestly commit malicious gradients.

## Why it stopped

Bounded toy evidence falsifies the standalone Byzantine-detection interpretation of plain Merkle-gradient commitments while preserving a narrower integrity/equivocation use case.

## Recommended next action

Stop this plain-Merkle claim as no-paper; next test should combine commitments with a semantic robust aggregation/audit rule and compare against robust aggregation alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Merkle-committed robust aggregation audit
- Success threshold: The combined protocol must match robust aggregation's final-model loss/accuracy within 2%, add reproducible audit evidence for at least 95% of challenged updates, and add less than 10% runtime overhead at the toy scale.
- Stop condition: Stop if Merkle commitments add no auditability beyond logged raw gradients, exceed 10% overhead at toy scale, or fail to preserve robust aggregation performance within 2%.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-gradient-byzantine-detection-toy-bf85e323b55d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
