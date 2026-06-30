# Lookahead Decoding Baseline on GB10 Unified Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lookahead-decoding-baseline-on-gb10-unified-memory-28b6d3f01e99`
Run ID: `lookahead-decoding-baseline-on-gb10-unified-memory-28b6d3f01e99-20260619T211721149251+0000`

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

- Provider-backed Research Facility batch: hf:MiniMaxAI/MiniMax-M3: enoch://research-facility/provider/hf:MiniMaxAI/MiniMax-M3/de473bf63e78

## What looked useful

GB10 prompt-lookup assisted generation showed 1.85x speedup with lookup 4 on the normal prompt and 2.26x-3.09x on the copy-heavy prompt, while lookup 4/8 slowed the repeated-prefix prompt to 0.97x/0.93x. Token-level checks matched greedy for lookup 4 normal and all repeated-prefix settings; lookup 8 normal diverged after 44 tokens.

## Boundaries and scale limits

Single 135M model, single GB10 GPU, three controlled prompts, 256 requested new tokens, three repeats per setting; not the full Lookahead Decoding paper implementation, not a custom serving backend, not a 7B+ or production workload validation.

## Claim scope

On one GB10 host using PyTorch 2.12.0+cu130 and Transformers prompt_lookup_num_tokens with HuggingFaceTB/SmolLM2-135M BF16, prompt-lookup lookahead improved 256-token decode throughput on normal and copy-heavy probes but slowed a repeated-prefix probe and one fast setting diverged from greedy after 44 generated tokens.

## Why it stopped

Bounded local baseline completed; result is useful but not paper-ready because it is a prompt-lookup proxy on one 135M model and includes prompt sensitivity plus a token-divergence case.

## Recommended next action

Run a bounded deepen follow-up that implements or uses a direct lookahead-decoding backend with accepted-token counters on a 1B-3B local model and stops unless it beats greedy by at least 1.3x while preserving token equivalence on most prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GB10 Lookahead Decode Acceptance Benchmark on a 1B-3B Model
- Success threshold: At least 1.3x mean elapsed-time speedup over greedy on two prompt classes with no token divergence for the first 256 generated tokens and no material UMA pressure increase.
- Stop condition: Stop if the direct implementation cannot preserve deterministic token equivalence, if speedup is below 1.1x on the first two prompt classes, or if memory/runtime exceeds the calibrated GB10 budget.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-decoding-baseline-on-gb10-unified-memory-28b6d3f01e99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
