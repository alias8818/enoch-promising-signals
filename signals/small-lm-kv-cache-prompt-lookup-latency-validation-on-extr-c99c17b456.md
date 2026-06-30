# Small-LM KV-cache prompt-lookup latency validation on extractive repeated-context prompts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-lm-kv-cache-prompt-lookup-latency-validation-on-extr-c99c17b456`
Run ID: `small-lm-kv-cache-prompt-lookup-latency-validation-on-extr-c99c17b456-20260527T080546482909+0000`

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

- Parent run decision: N-gram CPU Speculative Decode: enoch://control-plane/projects/n-gram-cpu-speculative-decode-241538880383/runs/n-gram-cpu-speculative-decode-241538880383-20260525T054001064067+0000
- Parent run decision: KV-cache prompt-lookup n-gram speculative decoding on natural repeated-context prompts: enoch://control-plane/projects/kv-cache-prompt-lookup-n-gram-speculative-decoding-on-natu-3ef72e79cc/runs/kv-cache-prompt-lookup-n-gram-speculative-decoding-on-natu-3ef72e79cc-20260525T055012159126+0000

## What looked useful

Across 54 repeated-context lookup measurements with max_draft=8, prompt lookup achieved 3.85x mean speedup, 2.94x median speedup, 75.7% mean forward-call reduction, 89.8% acceptance, and mean accepted span 6.73 tokens, with all 216 lookup decodes exactly matching greedy. Draft=1 and no-repeat controls showed little or no call reduction, supporting the mechanism that long accepted copied spans drive the speedup.

## Boundaries and scale limits

Tested one small pretrained model, Python/Transformers CPU implementation, 36 fixed prompts, 48 new tokens, no batching, no sampling, no optimized quantized inference engine, no natural trace corpus, and no production tail-latency load.

## Claim scope

On CPU-only Transformers distilgpt2 greedy decoding with KV cache, prompt-lookup verification exactly preserves greedy output and materially reduces latency on constructed extractive repeated-context prompts when copied multi-token spans are accepted.

## Why it stopped

Tier 2 direct evidence supports the mechanism on constructed repeated-context prompts but does not establish broad or publication-grade latency behavior across models, engines, corpora, or serving settings.

## Recommended next action

Stop as no-paper useful signal; the next bounded deepen test should run the same exactness, repeat-density, and draft-length ablations on an optimized quantized CPU inference engine with a natural prompt corpus binned by repeat density.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Repeat-density prompt-lookup latency validation in an optimized quantized CPU engine
- Success threshold: High repeat-density prompts achieve at least 1.5x median latency speedup and at least 40% forward-call reduction with 100% exact greedy-token identity; low repeat-density controls remain below 10% call reduction.
- Stop condition: Stop if exactness fails, if high repeat-density prompts do not exceed 1.2x median speedup, or if controls show comparable call reduction, indicating the effect is not specific to extractive repetition.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-kv-cache-prompt-lookup-latency-validation-on-extr-c99c17b456`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
