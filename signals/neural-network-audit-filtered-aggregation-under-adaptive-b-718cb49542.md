# Neural-network audit-filtered aggregation under adaptive Byzantine clients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `neural-network-audit-filtered-aggregation-under-adaptive-b-718cb49542`
Run ID: `neural-network-audit-filtered-aggregation-under-adaptive-b-718cb49542-20260527T210110926057+0000`

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

- Parent run decision: Local Byzantine Gradient Audit for Volunteer Training: enoch://control-plane/projects/local-byzantine-gradient-audit-for-volunteer-training-139f1687b456/runs/local-byzantine-gradient-audit-for-volunteer-training-139f1687b456-20260527T183903233675+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c397c3a251f1

## What looked useful

Neural audit-filtering showed strong mechanism support for rejecting adaptive Byzantine updates: 3.8% Byzantine keep rate in the main 30% Byzantine run and 16.5% in the 40% stress run, with low honest-drop rates. It did not satisfy the predeclared Tier 1 accuracy threshold of at least +0.03 over the best baseline.

## Boundaries and scale limits

Small synthetic logistic-regression task only; no deep model, real federated benchmark, multi-node training, privacy constraints, or attacker adaptation to the exact trained auditor parameters.

## Claim scope

In a pure NumPy federated logistic-regression simulation with non-iid synthetic clients, 30-40% adaptive Byzantine clients, and stealth-constrained harmful updates, a tiny neural audit filter substantially reduced accepted Byzantine updates but improved test accuracy by only about 1.4 percentage points over the best baseline.

## Why it stopped

Controlled small direct validation found mechanism support for filtering but early falsified the stated practical threshold: accuracy lift was +0.0144 in the main run and +0.0138 in the stress run, below the required +0.03.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should compare the neural auditor against explicit validation-loss and robust-statistics audit ablations on a small neural-network benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural auditor ablation on a small neural federated benchmark
- Success threshold: Neural audit mean attacked-test accuracy is at least 0.03 above the best non-neural audit or robust baseline, Byzantine keep rate is at most 0.50, honest drop rate is at most 0.35, and clean/no-attack accuracy drop is at most 0.01.
- Stop condition: Stop if neural audit fails to beat the best non-neural audit baseline by 0.03 absolute accuracy or if gains are explained by dropping more than 35% of honest updates.

## Evidence references

- Artifact root: `<local-path>/projects/neural-network-audit-filtered-aggregation-under-adaptive-b-718cb49542`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
