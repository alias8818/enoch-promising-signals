# Suffix-Array N-gram Draft vs Small Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-draft-vs-small-draft-model-for-speculative-decoding-36ac2b5750cf`
Run ID: `suffix-array-n-gram-draft-vs-small-draft-model-for-speculative-decoding-36ac2b5750cf-20260621T013812260571+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb2cc9445685

## What looked useful

The suffix n-gram proposer reached about 57k proposals/s versus 510 proposals/s for DistilGPT-2 in the medium run, but its target greedy match rate was 0.182 versus 0.636 and its acceptance proxy was 0.213 versus 0.735. This argues against suffix-only n-gram drafting as a quality-competitive drop-in replacement, while preserving a possible latency niche because proposal cost is negligible.

## Boundaries and scale limits

This run did not implement full multi-token speculative decoding, did not measure end-to-end serving throughput, and only tested GPT-2/DistilGPT-2 on WikiText-2 with up to 500 validation contexts and 500k suffix-table train tokens.

## Claim scope

On a bounded next-token proxy using GPT-2 as target, DistilGPT-2 as neural draft, and WikiText-2 held-out contexts, a suffix n-gram draft is much faster to propose tokens but substantially worse on target greedy-match and single-token speculative acceptance proxy.

## Why it stopped

Proxy/local evidence is mixed and not paper-ready: suffix n-gram drafting is orders of magnitude cheaper but much lower quality than the small neural draft on direct acceptance-oriented metrics.

## Recommended next action

Stop this run as no-paper evidence; if continuing, implement a bounded end-to-end multi-token speculative decoding benchmark that measures accepted tokens per target pass and wall-clock throughput for suffix-only, small-LM, and hybrid draft policies.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end multi-token suffix n-gram speculative decoding benchmark
- Success threshold: A suffix-only or hybrid policy must improve end-to-end tokens/s by at least 10% over the DistilGPT-2 draft baseline at matched output distribution checks, or demonstrate a clearly bounded deployment niche where it wins reproducibly.
- Stop condition: Stop if suffix-only and hybrid policies fail to beat the small-LM baseline on tokens/s or accepted tokens per target pass across two prompt distributions after tuning draft length and confidence thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-draft-vs-small-draft-model-for-speculative-decoding-36ac2b5750cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
