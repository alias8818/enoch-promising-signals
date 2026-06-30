# Noisy Anchor Extraction Replay for Compressed Agent Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `noisy-anchor-extraction-replay-for-compressed-agent-memory-53941c431f`
Run ID: `noisy-anchor-extraction-replay-for-compressed-agent-memory-53941c431f-20260613T211202106677+0000`

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

- Parent run decision: Anchor-Preserving Compressed Memory for Long-Context Agents: enoch://control-plane/projects/anchor-preserving-compressed-memory-for-long-context-agents-36f805127f4e/runs/anchor-preserving-compressed-memory-for-long-context-agents-36f805127f4e-20260613T204001598376+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffda7f9aacb9

## What looked useful

Layered confirmed-anchor memory reached 0.944 exact replay accuracy with 0.000 false-anchor rate, versus 0.333 accuracy and 0.667 false-anchor rate for the best non-layered baselines under late noisy distractors.

## Boundaries and scale limits

Synthetic templated corpus only; no real agent traces, LLM summarizer baseline, paraphrased queries, long-horizon drift, or multi-domain operational data were tested.

## Claim scope

In a deterministic 6-task, 36-query synthetic replay corpus with late noisy anchor distractors and an 8-anchor memory budget, confirmed-anchor layered memory replayed exact stable values more accurately than no-memory, transcript keyword search, and flat compressed anchor retrieval baselines.

## Why it stopped

Tier 1 controlled direct test produced a useful mechanism signal, but evidence remains synthetic and small, so this run closes as no-paper useful signal.

## Recommended next action

Run a bounded deepen test on real or realistic agent traces with paraphrased queries and an equal-budget LLM summarizer/retriever baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic Trace Noisy-Anchor Replay With Equal-Budget LLM Baseline
- Success threshold: Layered memory accuracy >= 0.80, false-anchor rate <= 0.10, and absolute accuracy gain >= 0.15 over the best equal-budget baseline.
- Stop condition: Stop if layered memory accuracy drops below 0.70 or fails to beat the best equal-budget baseline by at least 0.05 after the first 20 trace tasks.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-anchor-extraction-replay-for-compressed-agent-memory-53941c431f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
