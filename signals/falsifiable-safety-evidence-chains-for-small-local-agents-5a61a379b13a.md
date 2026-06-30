# Falsifiable Safety Evidence Chains for Small Local Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-safety-evidence-chains-for-small-local-agents-5a61a379b13a`
Run ID: `falsifiable-safety-evidence-chains-for-small-local-agents-5a61a379b13a-20260529T052913566775+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/91d47f7f6764

## What looked useful

Across a 240-case main run and 20 repeated seeds, the verified-chain monitor achieved 1.000 unsafe recall and 1.000 safe pass rate in the generated corpus, while action-only and rubber-stamp baselines had 0.667 unsafe recall because they missed all falsified-chain safe-action cases.

## Boundaries and scale limits

Synthetic rule-based traces only; no real LLM planner, no human audit study, no long-horizon agent loop, no real filesystem or network side effects, and no comparison to stronger typed policy or taint-tracking baselines.

## Claim scope

In a deterministic synthetic local-agent harness over file, shell, and network action proposals, a verified evidence-chain monitor detected missing, contradictory, and unsupported safety evidence that action-only and chain-presence baselines missed.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and supports the mechanism but not broad local-agent safety claims.

## Recommended next action

Run a bounded deepen follow-up with actual small local-model agent traces in a sandbox, using the same evidence-chain contract and stronger baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate verified safety evidence chains on real small local-agent traces
- Success threshold: Verified-chain monitor improves unsafe recall by at least 15 percentage points over the strongest baseline while keeping benign false blocks at or below 10 percent absolute.
- Stop condition: Stop if small models cannot emit parseable evidence chains above 70 percent of benign tasks, or if verified-chain false blocks exceed 20 percent before improving unsafe recall over the strongest baseline.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-safety-evidence-chains-for-small-local-agents-5a61a379b13a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
