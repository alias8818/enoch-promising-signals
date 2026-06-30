# Shallow-Layer Self-Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `shallow-layer-self-speculative-decoding-on-gb10-86a3d5f8a3c5`
Run ID: `shallow-layer-self-speculative-decoding-on-gb10-86a3d5f8a3c5-20260621T095555596472+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4ee2f99f8a58

## What looked useful

Shallow self-drafting has a measurable but insufficient mechanism: acceptance increases with depth from 7.2% at layer 6 to 45.3% at layer 11 of 12, yet the best exact speculative run is only 0.44x cached greedy throughput. Raw shared-head early exits are not enough for a GB10 speedup in this bounded implementation.

## Boundaries and scale limits

No production partial-layer KV cache, no trained early-exit head, no fused kernels, no large-model validation, no long-context serving workload, and fp16 exactness diverged between cached and no-cache greedy.

## Claim scope

On GB10 with GPT-2-small, fp32 greedy decoding, 4 prompts x 32 generated tokens, a conservative shallow-layer self-speculative prototype using the shared LM head exactly matches full greedy output but reaches at best 147.9 tok/s versus 333.4 tok/s for cached greedy.

## Why it stopped

Bounded direct GB10 evidence is useful but no-paper: the prototype is correct in fp32 and shows acceptance, but it is slower than cached greedy and does not validate the speedup claim.

## Recommended next action

Run one bounded deepen follow-up that implements true partial-layer KV-cache drafting or lightweight trained early-exit heads, and require exact greedy agreement plus at least 1.10x cached-greedy throughput before considering further scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Partial-KV Shallow Self-Speculative Decoder for GPT-2-small on GB10
- Success threshold: At least 1.10x cached-greedy tokens/sec on GPT-2-small-class prompts while preserving exact greedy output and reporting acceptance above 40% for the selected shallow depth.
- Stop condition: Stop if exactness fails, if acceptance remains below 30% at layer 10 or earlier, or if throughput remains below cached greedy after partial-cache/early-exit implementation.

## Evidence references

- Artifact root: `<local-path>/projects/shallow-layer-self-speculative-decoding-on-gb10-86a3d5f8a3c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
