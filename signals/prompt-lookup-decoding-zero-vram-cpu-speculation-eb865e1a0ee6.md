# Prompt Lookup Decoding: Zero-VRAM CPU Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-decoding-zero-vram-cpu-speculation-eb865e1a0ee6`
Run ID: `prompt-lookup-decoding-zero-vram-cpu-speculation-eb865e1a0ee6-20260628T081604811604+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8401bb97e671

## What looked useful

Best PLD config reduced target calls by 59.42% overall, 93.75% on exact-copy tasks, 84.50% on partial-copy tasks, and 0.00% on novel-control tasks, with exact match rate 1.0 and 63.00 us/token Python lookup overhead.

## Boundaries and scale limits

No real neural language model, KV cache, batching, GPU/CPU overlap, or wall-clock serving latency was tested. Target forward calls are a proxy for expensive model calls.

## Claim scope

In a deterministic CPU proxy, prompt lookup decoding preserved exact greedy output and reduced target verification calls for prompt-grounded copy and partial-copy continuations, but not for novel continuations.

## Why it stopped

Proxy-only useful signal: mechanism supported for copy-grounded continuations, but no real-model serving validation was performed.

## Recommended next action

Run the same PLD accounting on a real small causal LM with copy-heavy RAG/summarization prompts and report actual latency, acceptance, and quality parity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model prompt lookup decoding latency on copy-heavy prompts
- Success threshold: At least 20% wall-clock decode speedup on copy-heavy prompts with exact greedy parity and no more than 5% slowdown on novel-control prompts.
- Stop condition: Stop if PLD fails exact parity or if lookup/verification overhead removes speedup on copy-heavy prompts.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-decoding-zero-vram-cpu-speculation-eb865e1a0ee6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
