# Real-text GPT-2-tokenized IF pruning confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-gpt-2-tokenized-if-pruning-confirmation-36affd9035`
Run ID: `real-text-gpt-2-tokenized-if-pruning-confirmation-36affd9035-20260629T020742375710+0000`

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

- Parent run decision: IF-Guided Data Pruning for Tiny GPT-2 Pretraining: enoch://control-plane/projects/if-guided-data-pruning-for-tiny-gpt-2-pretraining-095fe9f2b3a8/runs/if-guided-data-pruning-for-tiny-gpt-2-pretraining-095fe9f2b3a8-20260629T014821937886+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f57fe012b74

## What looked useful

IF pruning preserves some nonrandom signal but loses badly to recency-preserving suffix pruning, indicating that plain inverse-frequency selection is the wrong standalone pruning rule for GPT-2-tokenized context.

## Boundaries and scale limits

Single corpus, pretrained GPT-2 small, inference-time context pruning only; no training-time pruning, architectural pruning, longer-context models, or multi-corpus robustness validation.

## Claim scope

On WikiText-2 real text tokenized with the GPT-2 tokenizer and evaluated with pretrained GPT-2, inverse-frequency-only inference-time context pruning is not competitive with suffix-only context pruning for fixed next-token NLL, though it can beat random retention at 25-50% keep rates.

## Why it stopped

Bounded direct inference-time test failed the success threshold: IF did not beat suffix at any keep rate, so this is an early negative/useful-signal result rather than full validation of all possible IF pruning variants.

## Recommended next action

Stop this IF-only confirmation as no-paper evidence; if continuing, test a bounded recency-aware IF hybrid against suffix and random on the same paired NLL protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recency-aware IF hybrid pruning on GPT-2-tokenized real text
- Success threshold: Hybrid pruning must beat suffix-only by at least 0.05 mean NLL at one or more keep rates with paired confidence intervals excluding zero, without regressing badly at other keep rates.
- Stop condition: Stop if hybrid does not beat suffix-only on WikiText-2 in a 512-example GPT-2 run or if gains vanish on the second corpus.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-gpt-2-tokenized-if-pruning-confirmation-36affd9035`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
