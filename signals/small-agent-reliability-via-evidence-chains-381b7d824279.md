# Small Agent Reliability via Evidence Chains

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-agent-reliability-via-evidence-chains-381b7d824279`
Run ID: `small-agent-reliability-via-evidence-chains-381b7d824279-20260609T115714048207+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11af1c80a1bf

## What looked useful

Path consistency alone can amplify false evidence chains, while requiring two independent supports per hop drove false-citation answer rate from 0.2710 to 0.0034 on 5,000 synthetic tasks, with coverage reduced to 0.4840 and answered accuracy 0.9930.

## Boundaries and scale limits

Synthetic deterministic tasks only; no real LLM planner, natural-language retrieval, human evidence labels, production tools, long-horizon workflows, or full-scale deployment validation.

## Claim scope

In a synthetic 3-hop noisy retrieval/tool benchmark, corroborated evidence chains reduced false-citation answers and wrong answered predictions compared with direct top-evidence and uncorroborated path-consistent baselines.

## Why it stopped

Proxy/mechanism evidence supports corroborated evidence chains in a synthetic benchmark but is not direct full validation for real small agents.

## Recommended next action

Stop this run as no-paper proxy evidence; run a bounded deepen follow-up with a real small LLM agent on a natural-language multi-hop retrieval/tool benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corroborated Evidence Chains for Small LLM Multi-Hop Tool QA
- Success threshold: Corroborated evidence chains reduce false-citation/support-error rate by at least 30 percent relative to the best baseline while preserving at least 60 percent of baseline answered accuracy or providing a clearly calibrated abstention benefit.
- Stop condition: Stop if corroboration fails to reduce support errors on real text traces, if the method collapses to unusable coverage below 25 percent without accuracy gains, or if citation verification cannot be labeled reliably.

## Evidence references

- Artifact root: `<local-path>/projects/small-agent-reliability-via-evidence-chains-381b7d824279`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
