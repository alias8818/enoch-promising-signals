# Prompt-Derived Suffix Tree Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-derived-suffix-tree-speculation-ee472bfa7d6d`
Run ID: `prompt-derived-suffix-tree-speculation-ee472bfa7d6d-20260604T180932084053+0000`

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

Copy-from-prompt and repeated-template cases reached about 99% best suffix acceptance, noisy templates reached 88.75%, and shuffled-order control stayed at 3.57%. External natural prose averaged 7.96% best acceptance across 16 windows and never reached the 20% useful threshold.

## Boundaries and scale limits

Benchmarks used regex word/punctuation tokens, oracle verification, one public-domain prose source with 16 windows, and controlled synthetic/copy cases. No production tokenizer, LLM verifier, latency measurement, cache accounting, or representative RAG/code/chat workload was tested.

## Claim scope

Prompt-derived suffix indexes can draft exact accepted tokens when continuations copy prompt spans or repeat structured templates, but they did not provide broadly useful acceptance on natural held-out prose in this bounded oracle proxy.

## Why it stopped

Proxy evidence supports the copy/template mechanism but early-falsifies broad natural-prose usefulness; this is not full validation and not paper-ready.

## Recommended next action

Stop this broad claim as no-paper evidence; run one bounded follow-up on copy-heavy RAG/document-QA traces with a real tokenizer and verifier latency before considering a narrower systems claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt suffix speculation on copy-heavy RAG traces
- Success threshold: At least 20% accepted generated tokens and at least 10% end-to-end latency improvement on copy-heavy examples, with no regression on low-copy examples beyond lookup overhead.
- Stop condition: Stop if accepted-token rate remains below 20% or latency improvement remains below 10% after controlling for copy rate and lookup overhead.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-derived-suffix-tree-speculation-ee472bfa7d6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
