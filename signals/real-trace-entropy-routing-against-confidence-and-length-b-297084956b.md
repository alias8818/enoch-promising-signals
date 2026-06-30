# Real-Trace Entropy Routing Against Confidence and Length Baselines

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-trace-entropy-routing-against-confidence-and-length-b-297084956b`
Run ID: `real-trace-entropy-routing-against-confidence-and-length-b-297084956b-20260529T074035686916+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: CPU Cascade Routing via Prompt Entropy: enoch://control-plane/projects/cpu-cascade-routing-via-prompt-entropy-144fcfa28318/runs/cpu-cascade-routing-via-prompt-entropy-144fcfa28318-20260529T032909300402+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/78abe1b60d0e

## What looked useful

Posterior entropy is a real uncertainty signal for recoverable cheap-model failures, but max-confidence is consistently as good or slightly better on this real-trace classification benchmark; length is near-useless.

## Boundaries and scale limits

10 seeds, 4,800 AG News test examples per seed, lightweight Naive Bayes classifiers; not real LLM token-generation traces, not latency-measured serving, and not multi-domain validation.

## Claim scope

On a Tier 1 real-text AG News cascade with saved cheap-model posterior traces, entropy routing improves over all-cheap and beats length/random, but does not outperform matched max-confidence routing.

## Why it stopped

Direct Tier 1 real-trace test failed the stated threshold: entropy accuracy averaged 0.8343 versus matched confidence 0.8362, with zero entropy wins and one tie across 10 seeds.

## Recommended next action

Stop this entropy-over-confidence follow-up as no-paper useful evidence; only revisit if a real LLM token-entropy trace benchmark is available with a predeclared matched-confidence comparison.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-entropy-routing-against-confidence-and-length-b-297084956b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
