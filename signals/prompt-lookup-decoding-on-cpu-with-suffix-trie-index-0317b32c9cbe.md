# Prompt Lookup Decoding on CPU with suffix-trie index

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-lookup-decoding-on-cpu-with-suffix-trie-index-0317b32c9cbe`
Run ID: `prompt-lookup-decoding-on-cpu-with-suffix-trie-index-0317b32c9cbe-20260611T042351507508+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dd153879496d

## What looked useful

Trie lookups stayed below 16 microseconds mean while direct scans reached 83-95 milliseconds at 65k prompt tokens; build time amortized in roughly 2-17 lookup queries, with high-entropy 65k prompts costing about 250 MiB incremental RSS in Python.

## Boundaries and scale limits

Synthetic token prompts only; pure-Python prototype; no integration with a real language model decoder, verifier loop, tokenizer traces, compact production data structure, or end-to-end tokens/s measurement.

## Claim scope

A bounded reversed suffix-trie index can accelerate the CPU lookup subproblem in prompt lookup decoding versus direct prompt scanning on synthetic token prompts up to 65,536 tokens with max_match=16.

## Why it stopped

Closed as no-paper useful signal because the local result validates only the lookup mechanism with synthetic/proxy evidence, not full prompt lookup decoding.

## Recommended next action

Implement the compact index in a real CPU decoder or trace replay harness and require at least 1.2x end-to-end decode throughput improvement on real prompts at equal output quality before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU prompt lookup decoding with compact suffix index
- Success threshold: At least 1.2x end-to-end decode throughput improvement over direct-scan PLD on real prompts, with equal output quality and less than 10 percent memory overhead relative to model/runtime memory.
- Stop condition: Stop if compact index build plus lookup overhead fails to improve end-to-end throughput by 10 percent on real traces or memory overhead exceeds practical serving limits.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-decoding-on-cpu-with-suffix-trie-index-0317b32c9cbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
