# Attention-head next-token speculation from cached patterns

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `attention-head-next-token-speculation-from-cached-patterns-60a4d22813f1`
Run ID: `attention-head-next-token-speculation-from-cached-patterns-60a4d22813f1-20260530T074502277773+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/acb90839f3ae

## What looked useful

Confirmation run over 20320 eval positions: attention-cache hit rates were top-1 0.1057, top-2 0.1476, top-4 0.2040, top-8 0.2679, top-16 0.3390. This beat global unigram at every k and shuffled attention by 7.8-11.7 percentage points, but lagged previous-token bigram at top-1/top-4 and only clearly beat it at top-16.

## Boundaries and scale limits

Tested only GPT-2-small, WikiText-2 train split windows, sequence length 128, 640 train windows and 160 eval windows. No integrated speculative decoder, verifier acceptance rate, wall-clock decoding speedup, larger models, longer contexts, or cross-corpus robustness were tested.

## Claim scope

On GPT-2-small attention tensors over WikiText-2 windows, cached per-head signatures of attended offset bucket plus attended token id carry held-out next-token signal beyond unigram frequency and shuffled-label attention controls, but are not a strong low-k standalone speculative candidate generator versus a previous-token bigram baseline.

## Why it stopped

Bounded direct probe found a real attention-cache next-token signal, but the simple cache is not competitive at low k with a previous-token bigram and no decoding speedup was demonstrated.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded test should evaluate a hybrid lexical-plus-attention cache inside a speculative decoding loop and require acceptance-rate or wall-clock improvement over n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid lexical and attention-cache speculative decoder probe
- Success threshold: At k<=8, hybrid candidates improve held-out next-token recall or verifier acceptance by at least 5 percentage points over previous-token bigram/trigram baselines while adding less than 10% candidate-generation overhead in the local prototype.
- Stop condition: Stop if the hybrid fails to beat n-gram-only baselines by at least 2 percentage points at k<=8 on the first 20000 held-out positions or if candidate-generation overhead exceeds any recall gain.

## Evidence references

- Artifact root: `<local-path>/projects/attention-head-next-token-speculation-from-cached-patterns-60a4d22813f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
