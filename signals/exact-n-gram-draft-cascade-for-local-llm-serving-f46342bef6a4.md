# Exact N-Gram Draft Cascade for Local LLM Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-n-gram-draft-cascade-for-local-llm-serving-f46342bef6a4`
Run ID: `exact-n-gram-draft-cascade-for-local-llm-serving-f46342bef6a4-20260604T194815029005+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae645af88749

## What looked useful

Best word-token cascade accepted 0.1888 tokens per evaluated position with 0.6380 coverage and 0.0374 draft-token acceptance; best byte-token cascade accepted 1.4910 bytes per evaluated position with 0.9974 coverage and 0.1869 draft-token acceptance. The mechanism exists, but standalone serving value is unproven.

## Boundaries and scale limits

No local LLM verifier, no GPU serving stack, no production tokenizer, no batching/KV-cache measurement, and only three small public text corpora. Byte-token results are mechanical text-stream evidence and should not be read as LLM token throughput.

## Claim scope

A dependency-free teacher-forcing benchmark on three small literary corpora shows that longest-first exact n-gram cascades can produce nonzero exact draft continuations and modestly outperform n=2/n=4 exact controls, but only at low word-token draft acceptance.

## Why it stopped

Bounded CPU teacher-forcing proxy completed; evidence is useful but insufficient for a paper-ready local LLM serving claim, and a long GB10 run is not justified before an integrated verifier benchmark.

## Recommended next action

Run a bounded deepen follow-up that plugs the exact n-gram cascade into a small local LLM verifier and compares wall-clock tokens/sec against no-draft on fixed chat/code prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated Local LLM Verifier Benchmark for Exact N-Gram Draft Cascades
- Success threshold: At least 10 percent wall-clock tokens/sec improvement over no-draft on both chat and code prompt subsets, with identical generated token sequences under greedy decoding and no hidden long-run GPU instability.
- Stop condition: Stop if integrated word/token acceptance remains below 0.25 accepted model tokens per generation step or wall-clock throughput fails to beat no-draft by 5 percent in a smoke-plus-main local benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/exact-n-gram-draft-cascade-for-local-llm-serving-f46342bef6a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
