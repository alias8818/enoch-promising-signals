# Prompt-Lookup Speculation on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-speculation-on-cpu-e88224fe46b8`
Run ID: `prompt-lookup-speculation-on-cpu-e88224fe46b8-20260609T180105269520+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/39c5b43f8902

## What looked useful

Main surrogate benchmark showed 1.89x mean speedup on verbatim repeats and 1.29x on edited repeats at dim 768, while novel continuations slowed to 0.33x. Sensitivity reached 4.49x for high-cost verbatim repeats but still slowed novel continuations.

## Boundaries and scale limits

No real transformer, tokenizer, KV-cache, sampling, or production CPU inference backend was tested; generated streams were controlled synthetic token sequences.

## Claim scope

In a bounded NumPy CPU surrogate with real prompt-lookup proposal logic and oracle greedy acceptance, prompt-lookup speculation speeds repeated-context continuations when verifier work is sufficiently expensive, but slows novel continuations and low-cost verifier settings.

## Why it stopped

Closed as a surrogate useful signal rather than full validation; evidence supports the mechanism but is not direct real-LLM evidence.

## Recommended next action

Run a bounded real CPU LLM benchmark using llama.cpp or an equivalent backend on repeated, edited-repeat, and novel prompts with greedy decoding and prompt-lookup speculation enabled.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM Prompt-Lookup Decoding Benchmark
- Success threshold: At least 1.2x tokens/sec improvement on repeated and edited-repeat prompt classes with no output mismatches, while the gating rule keeps novel-prompt slowdown under 5%.
- Stop condition: Stop if prompt-lookup decoding cannot be implemented in the selected CPU backend, outputs diverge under greedy decoding, or repeated-prompt speedup remains below 1.05x despite accepted draft rate above 70%.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-speculation-on-cpu-e88224fe46b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
