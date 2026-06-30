# Local-SGD with signed-bit sketch and periodic full-gradient verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-sgd-with-signed-bit-sketch-and-periodic-full-gradient-verification-e4ef24421e8f`
Run ID: `local-sgd-with-signed-bit-sketch-and-periodic-full-gradient-verification-e4ef24421e8f-20260619T155122297978+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8d7f05af6eeb

## What looked useful

Signed sketches are a plausible communication-saving baseline; full-gradient verification is a useful diagnostic for harmful update directions and improves train loss under heterogeneity, but the tested repair policy did not improve generalization and reduced compression from 27.43x to 6.19x in the main setting.

## Boundaries and scale limits

Convex synthetic proxy only; no neural-network training, real distributed transport, large datasets, or multi-node systems were tested.

## Claim scope

On synthetic non-IID distributed logistic regression, signed-bit worker-delta sketches preserved most accuracy with about 27x lower communication, but periodic full-gradient verification did not improve held-out accuracy enough to justify its added dense verification communication.

## Why it stopped

Bounded proxy evidence does not support the combined signed-bit sketch plus periodic full-gradient verification as a paper-ready improvement; verification repaired bad directions but failed to improve held-out accuracy.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a small neural network and only continue if verification improves held-out loss or accuracy over plain sign at comparable communication budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small neural-network test of signed Local-SGD verification under equal communication budget
- Success threshold: Verified signed-sketch improves held-out accuracy by at least 1 percentage point or held-out loss by at least 2% over plain sign while retaining at least 5x compression versus dense.
- Stop condition: Stop if verification fails to beat plain sign on held-out metrics in at least two of three seeds or if compression drops below 5x versus dense.

## Evidence references

- Artifact root: `<local-path>/projects/local-sgd-with-signed-bit-sketch-and-periodic-full-gradient-verification-e4ef24421e8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
