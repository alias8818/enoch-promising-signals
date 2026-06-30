# Suffix N-Gram Speculative Draft for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-n-gram-speculative-draft-for-cpu-inference-98770f6ee0aa`
Run ID: `suffix-n-gram-speculative-draft-for-cpu-inference-98770f6ee0aa-20260607T075325446078+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c5f32c29a0f0

## What looked useful

Recent suffix-copy drafting achieved 16.93x and 16.42x ideal target-call speedup with 0.999 and 0.968 draft acceptance on repeated-copy controls, but only 1.095x and 1.238x with 0.018 and 0.038 acceptance on natural Tiny Shakespeare and WikiText-2 streams. Lookup overhead for recent suffix copy was about 1.4-2.9 microseconds per speculative call in Python.

## Boundaries and scale limits

No real transformer verifier, tokenizer-specific evaluation, KV-cache rollback/update path, speculative sampling correction, or end-to-end tokens/sec measurement was run. Natural-text evidence covers two small corpora and proxy target streams only.

## Claim scope

Online suffix n-gram drafting was tested as an ideal target-call reduction mechanism on regex-tokenized Tiny Shakespeare and WikiText-2 validation streams, with natural and repeated-copy controls. It supports copy-heavy/repetitive-context drafting, not broad CPU LM latency acceleration.

## Why it stopped

Proxy evidence supports the suffix-copy mechanism in repeated contexts but natural-text gains are small and no direct transformer latency validation was performed.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a real CPU LM decoder integration measuring end-to-end tokens/sec on copy-heavy, code, RAG, and natural prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LM validation of recent suffix-copy speculative decoding
- Success threshold: At least 1.15x end-to-end tokens/sec improvement on two copy-heavy practical prompt classes with no statistically meaningful regression on natural prose, measured over at least 100 prompts per class.
- Stop condition: Stop if accepted spans remain strong but end-to-end speedup is below 1.05x on copy-heavy prompts, or if natural/code/RAG acceptance stays below 0.05 draft-token acceptance after tokenizer-accurate integration.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-speculative-draft-for-cpu-inference-98770f6ee0aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
