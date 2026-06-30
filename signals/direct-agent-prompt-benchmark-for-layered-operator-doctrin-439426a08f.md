# Direct Agent-Prompt Benchmark for Layered Operator Doctrine Memory

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `direct-agent-prompt-benchmark-for-layered-operator-doctrin-439426a08f`
Run ID: `direct-agent-prompt-benchmark-for-layered-operator-doctrin-439426a08f-20260620T104302640516+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Doctrine Memory: Layered Memory vs Retrieval on Repeated Agent Tasks: enoch://control-plane/projects/operator-doctrine-memory-layered-memory-vs-retrieval-on-repeated-agent-tasks-0547870d1fae/runs/operator-doctrine-memory-layered-memory-vs-retrieval-on-repeated-agent-tasks-0547870d1fae-20260620T100357176864+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c84521348d45

## What looked useful

Layered operator-doctrine prompts did not meet the predefined +20 percentage point all-pass compliance threshold over flat prompts. Qwen 0.5B showed better redaction/leak avoidance under layering but only 1/12 all-pass; Qwen 1.5B regressed under layering with 0/12 all-pass versus 2/12 flat.

## Boundaries and scale limits

Synthetic prompt-only benchmark; no real tool-use agent loop, long-horizon session memory, constrained decoding, production frontier model, or broad paraphrase/randomization coverage.

## Claim scope

Tier 1 controlled direct prompt benchmark on 12 adversarial/benign operator-doctrine memory cases using Qwen/Qwen2.5-0.5B-Instruct and Qwen/Qwen2.5-1.5B-Instruct with deterministic local generation.

## Why it stopped

Direct Tier 1 benchmark failed the stated success threshold on both tested models; this is an early direct falsification of the threshold for the tested prompt suite, not a full validation of all possible layered-doctrine designs.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should disentangle hierarchy from prompt length/schema effects before any larger model campaign.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-Matched Layered Doctrine Benchmark With Constrained JSON
- Success threshold: Layered prompt leak_rate at least 0.30 lower than both length-matched flat and shuffled-layer controls, with decision_accuracy no worse by more than 0.05 and all-pass compliance non-decreasing on at least two of three models.
- Stop condition: Stop if layered prompts fail to beat both controls on leak_rate by 0.15 or more after the first two models, or if constrained JSON removes the apparent layered redaction advantage.

## Evidence references

- Artifact root: `<local-path>/projects/direct-agent-prompt-benchmark-for-layered-operator-doctrin-439426a08f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
