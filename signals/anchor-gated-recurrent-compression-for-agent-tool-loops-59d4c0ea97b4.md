# Anchor-Gated Recurrent Compression for Agent Tool Loops

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-gated-recurrent-compression-for-agent-tool-loops-59d4c0ea97b4`
Run ID: `anchor-gated-recurrent-compression-for-agent-tool-loops-59d4c0ea97b4-20260602T215001485056+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6178637ba9c2

## What looked useful

Anchor gating produced a consistent +0.2294 mean accuracy gain over a same-size plain GRU and reduced non-anchor chatter state drift from 1.1908 to 0.0070, supporting the narrow mechanism that low-gated chatter updates can protect anchor facts in compressed recurrent state.

## Boundaries and scale limits

Synthetic categorical traces only; no real agent logs, natural language compression, LLM integration, production latency, retrieval baseline, sliding-window baseline, or GPT-2-small-class parameter-matched validation. Confirmation used a 60,608-parameter recurrent classifier for 500 training steps per model.

## Claim scope

On a synthetic typed agent-tool-loop retention task with sparse tool-result anchors, adversarial chatter, fixed recurrent state, and equal-parameter recurrent controls, anchor-gated recurrent updates improved final anchored fact prediction accuracy from 0.0350 to 0.2644 across three seeds.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but not direct agent-trace or LLM-scale evidence sufficient for publication.

## Recommended next action

Run a bounded deepen test on real or realistic agent traces with anchor labels, comparing anchor-gated recurrent compression against retrieval, sliding-window, and learned-summary baselines on downstream answer accuracy and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-Gated Compression on Realistic Agent Trace Replay
- Success threshold: Anchor-gated compression improves downstream answer accuracy by at least 10 percentage points over the strongest fixed-budget baseline or matches the strongest baseline with at least 25 percent lower memory/latency cost, with the effect replicated across three seeds or trace splits.
- Stop condition: Stop if anchor-gated compression fails to beat the strongest baseline by 5 percentage points on two independent trace splits or if anchor labels are unavailable/unreliable enough that the method cannot be evaluated directly.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-recurrent-compression-for-agent-tool-loops-59d4c0ea97b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
