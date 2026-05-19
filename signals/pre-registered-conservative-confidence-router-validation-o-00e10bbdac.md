# Pre-registered conservative confidence-router validation on a second direct text task

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pre-registered-conservative-confidence-router-validation-o-00e10bbdac`
Run ID: `pre-registered-conservative-confidence-router-validation-o-00e10bbdac-20260519T000304721875+0000`

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

- Internal Enoch project: Pre-registered conservative confidence-router validation on a second direct text task: internal_generated:pre-registered-conservative-confidence-router-validation-o-00e10bbdac

## What looked useful

Second direct text task confirmation: the conservative 0.25 pp validation-margin router passed all per-seed accuracy and cost gates on AG News, with mean cascade accuracy 92.1842% vs strong 92.3605%, worst bootstrap lower bound -0.5395 pp, and mean strong-call reduction 74.0816%. Ablations showed zero-margin selection failed cost and 1.0 pp selection failed noninferiority.

## Boundaries and scale limits

Evidence is limited to local scikit-learn text classifiers and strong-model invocation reduction. It does not validate LLM/API routing, production latency, dollar cost, batching, shared-feature serving, or cross-domain robustness beyond this AG News follow-up and the prior 20 Newsgroups lineage.

## Claim scope

On AG News 4-class text classification, a pre-registered conservative confidence-router using ComplementNB confidence to gate a LinearSVC fallback passed five fixed-seed held-out noninferiority at a 1 percentage point paired-bootstrap margin while reducing strong-model calls by at least 71% on every seed.

## Why it stopped

Medium direct validation succeeded, but the evidence is still a local classifier cascade and does not meet the strict paper gate for deployed cost/latency or LLM-router claims.

## Recommended next action

Stop this run as no-paper useful signal; next, if pursuing publication, freeze the rule and run a bounded multi-dataset package with shared-feature latency or explicitly scope the claim to strong-call reduction only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen-rule multi-dataset confidence-router package with shared-feature latency accounting
- Success threshold: Every dataset and seed has cascade-minus-strong paired-bootstrap 95% CI lower bound >= -1.0 pp and strong-call reduction >= 25%; shared-feature implementation shows positive median latency/compute savings if latency is claimed.
- Stop condition: Stop if any dataset fails the per-seed noninferiority gate under the frozen rule, any dataset fails the 25% strong-call reduction gate, or shared-feature timing fails while the intended claim requires latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/pre-registered-conservative-confidence-router-validation-o-00e10bbdac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
