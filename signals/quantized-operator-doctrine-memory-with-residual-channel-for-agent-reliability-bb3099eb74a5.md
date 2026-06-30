# Quantized Operator-Doctrine Memory with Residual Channel for Agent Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-operator-doctrine-memory-with-residual-channel-for-agent-reliability-bb3099eb74a5`
Run ID: `quantized-operator-doctrine-memory-with-residual-channel-for-agent-reliability-bb3099eb74a5-20260628T065705339511+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0d7c79acde9e

## What looked useful

Quantization collision ratio was 0.800. Quantized-only accuracy was 0.158, matching no-memory and failing all exception queries. Quantized-with-residual accuracy was 1.000, matching layered doctrine memory, but used 1.33x the layered storage proxy because residuals were required for 100% of operator-key slots.

## Boundaries and scale limits

Synthetic structured events only; no real LLM agent traces, no natural-language doctrine extraction, no learned quantizer, no direct task-completion metric, and only a simple storage proxy. The residual channel covered every operator-key slot in the medium run, so the result does not show compression advantage over exact layered doctrine memory.

## Claim scope

In a deterministic synthetic repeated-agent replay with 6 operators, 5 doctrine keys, 240 queries, noisy distractors, stale updates, and exact exception values, coarse quantized operator-doctrine memory alone failed exact recall, while adding an exact residual channel restored recall to the layered exact-memory baseline.

## Why it stopped

Bounded synthetic evidence supports the residual recovery mechanism but does not support the stronger architecture claim because reliability required dense exact residual storage and did not beat a simpler exact layered baseline.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should evaluate an adaptive sparse residual gate on non-synthetic or LLM-generated traces and require a compression/reliability Pareto win over exact layered doctrine memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive sparse residual gate for operator-doctrine memory on generated agent traces
- Success threshold: At least 95% exact active-doctrine recall and 95% exception recall, no more than 1 percentage point below exact layered doctrine memory, with storage/token cost at or below 0.75x the exact layered baseline.
- Stop condition: Stop if residual fraction exceeds 0.50 of operator-key slots or exact recall falls below 90% after the first 200 trace queries.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-operator-doctrine-memory-with-residual-channel-for-agent-reliability-bb3099eb74a5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
