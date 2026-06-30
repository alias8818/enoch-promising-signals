# N-gram speculative draft for CPU transformer serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-cpu-transformer-serving-f0c9abdb212e`
Run ID: `n-gram-speculative-draft-for-cpu-transformer-serving-f0c9abdb212e-20260608T084111666303+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/97e96394eeb2

## What looked useful

Prompt-local lookup reached 4.51 mean accepted regex tokens on Python stdlib with 8-token context and 8-token drafts, and 3.37 mean accepted byte tokens with 4-byte context and 8-byte drafts. Prose results were modest and long contexts often collapsed hit rate. Lookup overhead was under a few microseconds per position in Python.

## Boundaries and scale limits

No real transformer tokenizer, target model, speculative verification kernel, or end-to-end CPU serving latency was measured. Results are capped at 1M train tokens and 200k held-out test tokens per corpus/tokenizer proxy.

## Claim scope

In a local acceptance proxy over WikiText-2, Tiny Shakespeare, and Python stdlib text, prompt-local n-gram lookup can yield multi-token accepted drafts in repetitive/code-like contexts, while global static n-gram drafting is not consistently strong.

## Why it stopped

Closed as no-paper useful signal because the evidence is acceptance-proxy only and supports a narrow prompt-local mechanism, not publication-grade end-to-end CPU transformer serving speedup.

## Recommended next action

Run a bounded deepen test in a real CPU inference stack with a model tokenizer and wall-clock speculative decoding on repeated-code versus prose prompts; stop treating global static n-grams as a broad serving optimization until that direct test passes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU speculative decoding test for prompt-local n-gram drafts
- Success threshold: At least 25% wall-clock tokens/sec improvement on repeated-code prompts and no more than 5% regression on prose prompts, over at least 100 prompts per class.
- Stop condition: Stop if accepted tokens per target call is below 1.25 on code prompts or if lookup plus verification overhead causes more than 5% prose regression.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-cpu-transformer-serving-f0c9abdb212e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
