# LLM Small-Agent Evidence Ledger on Labeled Retrieval Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-small-agent-evidence-ledger-on-labeled-retrieval-tasks-dd12f1d09c`
Run ID: `llm-small-agent-evidence-ledger-on-labeled-retrieval-tasks-dd12f1d09c-20260524T072713026673+0000`

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

- Parent run decision: Small-Agent Evidence Ledger: enoch://control-plane/projects/small-agent-evidence-ledger-339c9bb6b39b/runs/small-agent-evidence-ledger-339c9bb6b39b-20260524T070832042830+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2f1443c8e737

## What looked useful

At 0% label noise the ledger reached 1.000 accuracy and 1.000 citation precision, versus 0.4816 accuracy for top1 and 0.2507 for unlabeled majority. At 25% randomized label corruption the ledger still improved accuracy to 0.7622 but citation precision fell to 0.8411, showing dependence on reliable evidence labels.

## Boundaries and scale limits

Synthetic fictional entities only; deterministic claim extraction; no real LLM reading/generation loop; 12 seeds x 240 tasks; label quality controlled by randomized corruption rather than a trained evidence classifier or real retrieval annotations.

## Claim scope

In a controlled synthetic labeled-retrieval benchmark with adversarially ranked and repeated conflicting evidence, an explicit evidence-ledger agent using reliable support/contradict/irrelevant labels improved exact answer accuracy and citation precision over retrieval-only and unlabeled majority baselines.

## Why it stopped

Tier 1 controlled direct test produced mechanism support but not paper-positive evidence because LLM extraction and real retrieval datasets were proxied.

## Recommended next action

Run one bounded real-data follow-up using a small local instruction model on a FEVER/SciFact-style labeled retrieval subset to test whether the ledger benefit survives real model extraction and natural label errors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real labeled retrieval ledger test with a small instruction model
- Success threshold: Ledger accuracy improves over both baselines by >=0.10 absolute on the real-data subset and citation precision is >=0.85, with no collapse under observed label/extraction errors.
- Stop condition: Stop if the ledger fails to beat either baseline by 0.05 absolute accuracy on a 100-example smoke split or if citation precision is below 0.75, because the synthetic mechanism would not transfer to real-data evidence handling.

## Evidence references

- Artifact root: `<local-path>/projects/llm-small-agent-evidence-ledger-on-labeled-retrieval-tasks-dd12f1d09c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
