# Commitment-reveal gradient validation for volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commitment-reveal-gradient-validation-for-volunteer-training-54526d2e469c`
Run ID: `commitment-reveal-gradient-validation-for-volunteer-training-54526d2e469c-20260527T155943944628+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5b7333bad206

## What looked useful

Commit-reveal audit filtering rejected simple sign-flip and random malicious gradients at about 98%+ rates while preserving final synthetic accuracy, but it rejected about 20% of honest clean non-IID updates and accepted 81% of audit-aligned adaptive updates.

## Boundaries and scale limits

No real dataset, no real volunteer network, no privacy constraints, no Sybil model, no hidden rotating audit set, and no large-model or long-horizon training. The task is linearly separable enough that final accuracy saturates for many defenses.

## Claim scope

Small synthetic federated-learning benchmark with 20 clients, 30% malicious volunteers, 5 seeds, and public audit-gradient cosine/norm filtering after hash commitment.

## Why it stopped

Bounded synthetic evidence is mixed: useful for simple malicious-gradient detection, but not a full volunteer-training validation and not robust to audit-aligned adaptive updates.

## Recommended next action

Stop this run as no-paper useful signal; next run should test hidden rotating audit batches on a harder real workload before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hidden rotating audit batches for commitment-reveal volunteer gradient validation
- Success threshold: Hidden rotating audit accepts less than 10% of adaptive malicious updates, rejects less than 10% of honest updates, and matches or exceeds coordinate median final quality within one standard error.
- Stop condition: Stop as negative if adaptive malicious acceptance remains above 25% or honest rejection remains above 20% after threshold calibration.

## Evidence references

- Artifact root: `<local-path>/projects/commitment-reveal-gradient-validation-for-volunteer-training-54526d2e469c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
