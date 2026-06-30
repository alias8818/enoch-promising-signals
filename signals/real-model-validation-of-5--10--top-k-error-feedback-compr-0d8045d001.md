# Real-model validation of 5%-10% top-k error-feedback compression for non-IID local training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-validation-of-5--10--top-k-error-feedback-compr-0d8045d001`
Run ID: `real-model-validation-of-5--10--top-k-error-feedback-compr-0d8045d001-20260608T004145316931+0000`

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

- Parent run decision: Top-k Gradient Compression for Volunteer Local Training: enoch://control-plane/projects/top-k-gradient-compression-for-volunteer-local-training-d79070a77d8f/runs/top-k-gradient-compression-for-volunteer-local-training-d79070a77d8f-20260607T203515227595+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b929845421d7

## What looked useful

Mean final accuracy was dense 0.7903, 10% top-k EF 0.7819, 5% top-k EF 0.7739, 10% no-EF 0.7644, and 5% no-EF 0.7436. Dense gaps were 0.84 percentage points for 10% EF and 1.64 points for 5% EF, satisfying the bounded threshold; EF improved over no-EF by about 1.7 and 3.0 points respectively.

## Boundaries and scale limits

Small CNN, MNIST only, 350 samples per client, 25 rounds, 3,000-example test cap, full client participation, no real network transport, no byte-level index accounting, no large models, no language models, no client dropout, and only three seeds.

## Claim scope

In a Tier 1 small direct MNIST experiment with a 101k-parameter CNN, 12 Dirichlet non-IID clients, one local SGD epoch per communication round, and three seeds, 5%-10% top-k update compression with per-client error feedback stayed within 2 percentage points of dense FedAvg after 25 rounds and beat matching no-error-feedback controls.

## Why it stopped

Small direct validation produced useful mechanism support but is not publication-grade evidence; paper gate remains closed.

## Recommended next action

Run a bounded medium deepen test on a harder real dataset/model with full test evaluation, at least five seeds, partial client participation, and byte-level communication accounting before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-dataset validation of 5%-10% top-k error-feedback compression under partial participation
- Success threshold: Both 5% and 10% EF variants finish within 2 percentage points of dense FedAvg mean accuracy, beat matching no-EF controls by at least 1 percentage point, and reduce encoded communication bytes versus dense under the stated accounting.
- Stop condition: Stop if either EF variant falls more than 3 percentage points behind dense in at least four of five seeds, or if encoded bytes erase the communication advantage over dense.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-validation-of-5--10--top-k-error-feedback-compr-0d8045d001`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
