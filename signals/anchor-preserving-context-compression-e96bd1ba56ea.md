# Anchor-Preserving Context Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-preserving-context-compression-e96bd1ba56ea`
Run ID: `anchor-preserving-context-compression-e96bd1ba56ea-20260619T155311944098+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e23f283e0f4

## What looked useful

Anchor-preserving compression reached 1.0000 exact-match accuracy at 0.1865 mean compression ratio, versus 0.3097 for tail truncation and 0.6806 for flat keyword selection. Flat keyword selection preserved many anchor mentions but produced a 0.1236 false-recall rate; anchor-preserving produced 0.0 false recall in this probe.

## Boundaries and scale limits

Synthetic 120-task local CPU benchmark only; no real operator traces, no LLM-generated summaries, no long-context model inference, no human evaluation, and no full-scale serving validation.

## Claim scope

In a deterministic synthetic repeated-agent replay benchmark with explicit durable anchor tags, query-blind anchor-preserving compression retained more exact answerable facts than tail truncation and flat keyword selection at similar compression ratios.

## Why it stopped

Closed as no-paper useful signal because the mechanism was supported only on a synthetic deterministic benchmark, not on real traces or model-in-the-loop evidence.

## Recommended next action

Run the same query-blind anchor-preserving compression comparison on real multi-session agent traces with an LLM or separate extractor as the downstream answerer before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-preserving compression on real repeated-agent traces
- Success threshold: Anchor-preserving compression must improve exact answer accuracy by at least 0.10 over the strongest baseline at a matched compression ratio and must not increase false-recall rate by more than 0.02 absolute.
- Stop condition: Stop if anchor-preserving is within 0.03 accuracy of the strongest baseline, increases false recall by more than 0.02, or requires query-aware compression to show benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserving-context-compression-e96bd1ba56ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
