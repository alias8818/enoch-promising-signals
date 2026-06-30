# Suffix-Array Speculative Decoding for Small Local Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-for-small-local-models-628ef309d5eb`
Run ID: `suffix-array-speculative-decoding-for-small-local-models-628ef309d5eb-20260528T040751004878+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58cdd723e86b

## What looked useful

Suffix-array drafting consistently beat the n-gram control but remained weak in absolute terms: on the 80k-token/96-prompt draft-4 run it accepted 393 of 9552 drafted tokens (4.11%) and reached 1.146 emitted tokens per verifier forward versus 1.089 for n-gram majority. Draft length 2 raised acceptance to 7.72% but reduced amortization to 1.119 tokens per forward.

## Boundaries and scale limits

Evidence is limited to GPT-2, WikiText-2, greedy decoding, 24-96 prompts, 30k-80k indexed corpus tokens, and verifier-forward-count amortization. It does not measure real KV-cache serving latency, sampling behavior, larger models, code/chat domains, or large suffix-array memory/cache behavior.

## Claim scope

On GPT-2 greedy verification over WikiText-2 validation prompts, a suffix-array exact-match draft proposer built from 30k-80k WikiText-2 train tokens produced accepted speculative tokens and modestly improved emitted tokens per verifier forward versus a matched n-gram majority control.

## Why it stopped

No-paper useful signal: this direct small-model proxy showed only small verifier-forward amortization and low draft acceptance, and did not validate actual serving latency.

## Recommended next action

Stop the paper path for general WikiText-style generation; the best bounded next action is a KV-cache-aware follow-up on code or local-document corpora where long exact suffix matches are more plausible.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache suffix-array drafting on code/local-document completion
- Success threshold: At least 1.25x wall-clock tokens/sec over greedy GPT-2-class baseline on held-out code/local-document prompts, with acceptance gains over both n-gram majority and prompt-lookup controls.
- Stop condition: Stop if KV-cache serving speedup is below 1.10x or suffix-array acceptance remains below 10% drafted tokens on the target domain after bounded tuning.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-for-small-local-models-628ef309d5eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
