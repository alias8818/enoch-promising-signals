# Rolling N-gram Draft Buffer on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-n-gram-draft-buffer-on-cpu-6458a0bc7886`
Run ID: `rolling-n-gram-draft-buffer-on-cpu-6458a0bc7886-20260603T162240886587+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/247ced2927e2

## What looked useful

Mechanism works cheaply in a bounded proxy, but the best accepted-token lift over a simple 1-gram baseline is small and not paper-ready. Longer contexts improve precision per proposal but are sparse.

## Boundaries and scale limits

This run did not use BPE/model tokens, an LLM verifier, chat/code corpora, compiled implementation, or end-to-end speculative decoding throughput. It was a single-process Python benchmark over about 261k total regex tokens.

## Claim scope

On three public-domain English text streams with regex tokenization, a CPU online rolling n-gram buffer can propose accepted draft runs from prior context occurrences; a 2-gram buffer reached 0.1615 accepted tokens per position versus 0.1548 for a previous-same-1-gram baseline, while longer contexts traded coverage for precision.

## Why it stopped

Proxy evidence supports the mechanism but does not validate real speculative-decoding speedup; publication would require tokenizer/model-serving evidence.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with real BPE tokens and an end-to-end verifier-loop throughput measurement before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE-token verifier-loop test for CPU rolling n-gram draft buffers
- Success threshold: At least 5% end-to-end tokens/s improvement over no-draft and the previous-1-gram control on one realistic workload, with CPU draft overhead below 10% of verifier time and no regression larger than 2% on the other tested workloads.
- Stop condition: Stop if BPE-token acceptance falls below 0.05 accepted tokens per position for all workloads or if optimized buffer overhead exceeds any verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-n-gram-draft-buffer-on-cpu-6458a0bc7886`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
