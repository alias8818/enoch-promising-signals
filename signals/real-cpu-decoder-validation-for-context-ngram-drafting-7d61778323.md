# Real CPU Decoder Validation for Context-Ngram Drafting

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-cpu-decoder-validation-for-context-ngram-drafting-7d61778323`
Run ID: `real-cpu-decoder-validation-for-context-ngram-drafting-7d61778323-20260523T201641060729+0000`

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

- Parent run decision: Context-Ngram Speculative Decoding CPU: enoch://control-plane/projects/context-ngram-speculative-decoding-cpu-a6de05d8db60/runs/context-ngram-speculative-decoding-cpu-a6de05d8db60-20260523T144434496393+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f4aa93715e73

## What looked useful

Context n-gram drafting produced identical greedy token streams to vanilla decoding and achieved 3.05x mean speedup on three repeated-context prompts, reducing model calls from 97 to 17-28 in the strongest cases. This supports the mechanism but is not paper-ready.

## Boundaries and scale limits

One small pretrained model, four hand-built prompts, greedy decoding only, Python/Hugging Face implementation, no production serving engine, no large-model or broad corpus validation, and the mixed-context control became repetitive during generation.

## Claim scope

In a controlled small CPU benchmark with distilgpt2, exact greedy context-ngram draft verification preserved token-identical output and reduced model calls/speeded decoding on repeated-context prompts.

## Why it stopped

Tier 1 direct CPU validation completed; evidence is useful but too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with a corpus-derived prompt suite, explicit non-repetition controls, repeated trials, and either a stronger CPU-serving stack or several GPT-2-class models before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-Controlled CPU Benchmark for Exact Context-Ngram Drafting
- Success threshold: Median speedup >= 1.25x on repeated-context prompts, p10 speedup >= 1.0x, non-repetitive median slowdown no worse than 10%, and zero token mismatches versus vanilla greedy.
- Stop condition: Stop if any token mismatch occurs, repeated-context median speedup is below 1.10x, or non-repetitive controls show more than 20% median slowdown after implementation-level tuning.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-decoder-validation-for-context-ngram-drafting-7d61778323`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
