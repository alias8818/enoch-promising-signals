# Suffix-automaton n-gram draft with zero VRAM on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-automaton-n-gram-draft-with-zero-vram-on-gb10-16c36dac7462`
Run ID: `suffix-automaton-n-gram-draft-with-zero-vram-on-gb10-16c36dac7462-20260629T093527698727+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d677fc24f5fe

## What looked useful

The suffix automaton achieved long accepted prefixes on repetitive prompt/code-like streams, but fixed n-gram tables matched or beat its acceptance while running much faster. On 50k-token runs, SAM query throughput was about 16k-41k positions/s versus roughly 30k-274k positions/s for n-grams, with SAM peak traced memory around 15-22 MB.

## Boundaries and scale limits

Tested only on local/proxy token streams up to 50k tokens per corpus with exact-token acceptance metrics. No real LLM tokenizer, neural verifier, GPU verification path, verifier batching, or end-to-end speculative decoding latency was measured.

## Claim scope

A CPU-only token suffix automaton can act as a zero-VRAM draft source for repeated local token streams, but in this bounded proxy it does not outperform simple fixed-order n-gram baselines once query throughput and memory are considered.

## Why it stopped

Proxy evidence is useful but not paper-positive: SAM is viable for repeated-context drafting, yet does not clearly beat simpler n-gram baselines and no neural verifier or end-to-end latency path was tested.

## Recommended next action

Stop this run as no-paper evidence; if pursued, run one bounded real-tokenizer verifier integration that compares SAM draft, fixed n-gram draft, and no draft on end-to-end tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-tokenizer verifier benchmark for suffix-automaton drafts
- Success threshold: SAM must improve end-to-end generated tokens/sec by at least 10% over both no-draft and fixed n-gram draft controls at equal output quality on a bounded local verifier workload.
- Stop condition: Stop if SAM acceptance is not higher than fixed n-gram acceptance or if CPU draft overhead removes any end-to-end throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-automaton-n-gram-draft-with-zero-vram-on-gb10-16c36dac7462`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
