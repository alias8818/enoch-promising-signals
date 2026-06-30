# N-gram CPU Draft Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-cpu-draft-speculative-decoding-e3a8465c1f5f`
Run ID: `n-gram-cpu-draft-speculative-decoding-e3a8465c1f5f-20260604T175917491094+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a754244e1744

## What looked useful

Repeated-context traces achieved about 89-94% verifier-call reduction with sub-microsecond Python n-gram lookup overhead, while tiny Shakespeare achieved only 2.0% word-token reduction and 22.2% byte-token reduction with very low proposal acceptance.

## Boundaries and scale limits

No real LLM verifier, no BPE tokenizer, no KV-cache or batched target-forward measurement, no production serving stack, and only one natural-text corpus. Results are mechanism evidence, not end-to-end speculative decoding validation.

## Claim scope

Trace-level CPU n-gram prompt-lookup drafting over five windows each of tiny Shakespeare plus synthetic repeated code, legal, and QA corpora. The mechanism reduces verifier iterations strongly only on repetition-heavy traces; broad natural-text usefulness is not supported by this run.

## Why it stopped

Proxy trace evidence is mixed: strong on synthetic repetition controls but weak on broad natural text, so it is not a paper-positive validation.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next bounded test is a real small-model verifier benchmark using the model tokenizer and end-to-end latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model end-to-end verifier benchmark for CPU n-gram prompt lookup
- Success threshold: At least 1.2x end-to-end speedup on repeated or retrieval-heavy prompts with no more than 5% slowdown on natural prompts, measured over real model decoding.
- Stop condition: Stop if real-model overhead erases the trace-level verifier-call savings or if natural/code prompt acceptance stays below 10% proposed-token acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cpu-draft-speculative-decoding-e3a8465c1f5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
