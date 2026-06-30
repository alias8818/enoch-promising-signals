# Prompt-Suffix N-Gram Cache for Zero-VRAM Speculative Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-suffix-n-gram-cache-for-zero-vram-speculative-drafting-1836862b2b78`
Run ID: `prompt-suffix-n-gram-cache-for-zero-vram-speculative-drafting-1836862b2b78-20260528T121143429486+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/69f4e9668cc9

## What looked useful

Mechanism is real for repeated spans: synthetic repeated prompts averaged about 5.9x estimated target-call reduction in the confirmation run. Generic real text was sparse: 7 of 20 Wikitext prompts exceeded 1.1x estimated target-call reduction, median real-text speedup was 1.008x, and mean was 1.694x due to a minority of repetitive prompts.

## Boundaries and scale limits

Tested with distilgpt2, 3 synthetic repeated prompts, 1 synthetic unique control, and 20 Wikitext prompts up to 768 prompt tokens and 128 generated tokens. No end-to-end verifier latency, modern 7B+ model, chat/code/RAG trace corpus, batching, or sampling validation was run.

## Claim scope

A CPU prompt-suffix n-gram cache can provide zero-VRAM speculative draft tokens that match a small greedy target model in repeated-prompt contexts, but benefits are sparse on generic Wikitext prose.

## Why it stopped

Replay evidence supports an opportunistic mechanism but not a broad standalone speculative drafting claim; this is not full validation and is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should measure actual wall-clock speculative verification on repetition-heavy code/RAG/tool-trace prompts with a generic-text control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Wall-clock prompt-suffix n-gram speculative decoding on repetition-heavy traces
- Success threshold: At least 1.2x median wall-clock speedup on the repetition-heavy set, no median slowdown worse than 2 percent on generic controls, and exact greedy-token equality versus baseline.
- Stop condition: Stop if cache-hit telemetry predicts fewer than 0.2 accepted drafted tokens per output token on the repetition-heavy set or if end-to-end verifier overhead eliminates estimated call savings.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-n-gram-cache-for-zero-vram-speculative-drafting-1836862b2b78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
