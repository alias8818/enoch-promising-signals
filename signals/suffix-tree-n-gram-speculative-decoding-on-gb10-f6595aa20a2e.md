# Suffix-tree n-gram speculative decoding on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-speculative-decoding-on-gb10-f6595aa20a2e`
Run ID: `suffix-tree-n-gram-speculative-decoding-on-gb10-f6595aa20a2e-20260611T074417494371+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d5a821022275

## What looked useful

Suffix-majority ctx16 draft8 estimated 3.61x net speed on copy-span streams, but only 1.03-1.07x on WikiText-2 word tokens with median accepted tokens zero. Phrase-mix performance was strong but matched or slightly beaten by fixed 4-gram with a much smaller table.

## Boundaries and scale limits

No real LLM target, no subword tokenizer acceptance test, no serving backend integration, no production prompt traces, and no long/full-scale GB10 inference benchmark. CUDA calibration used random weights only to estimate short verification window cost.

## Claim scope

Bounded local proxy: suffix-indexed n-gram drafting on 60k-token synthetic and WikiText-2 word-token streams, with GB10 random-transformer verification-shape calibration. The mechanism is useful on copy/repetition-heavy streams but weak on the local natural-language proxy.

## Why it stopped

Proxy/early falsification of a broad natural-language suffix-tree n-gram speculative decoding speedup claim; evidence supports only recurrence-heavy workloads and is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use real LLM tokenization and code/chat/RAG trace prompts against prompt-lookup and fixed n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix n-gram drafting on recurrence-heavy LLM traces
- Success threshold: At least 15% end-to-end tokens/s improvement over the best non-suffix drafter on recurrence-heavy traces, with no correctness regressions and no slowdown greater than 5% on natural-text controls.
- Stop condition: Stop if median accepted tokens remain zero on recurrence-heavy real-token traces or if suffix lookup/table overhead removes the speedup versus fixed n-gram or prompt-lookup baselines.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-decoding-on-gb10-f6595aa20a2e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
