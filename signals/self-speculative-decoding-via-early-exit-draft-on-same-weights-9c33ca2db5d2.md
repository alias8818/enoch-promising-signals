# Self-speculative decoding via early-exit draft on same weights

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-speculative-decoding-via-early-exit-draft-on-same-weights-9c33ca2db5d2`
Run ID: `self-speculative-decoding-via-early-exit-draft-on-same-weights-9c33ca2db5d2-20260620T125755131229+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/af51574fccbe

## What looked useful

Naive same-weight early exits show the expected accuracy/cost tradeoff: shallow exits are cheap but rarely match full-model tokens, while late exits accept more tokens but remain too expensive to beat full greedy decoding. Increasing gamma from 4 to 8 at depths 10 and 11 reduced estimated speed further.

## Boundaries and scale limits

Single GPT-2 small-class pretrained model; 24 fallback text prompts; greedy decoding only; no KV-cache optimized speculative serving kernel; no trained auxiliary exit heads; no larger model families or stochastic decoding tests.

## Claim scope

On openai-community/gpt2 with zero-training early exits that reuse the final layer norm and tied LM head, same-weight early-exit drafting did not produce a speedup under exact greedy speculative verification. The best tested gamma=4 setting, depth 11/12, accepted 35.86% of draft tokens and had an estimated 0.794x speed versus greedy in the measured no-cache cost model.

## Why it stopped

Bounded direct test on GPT-2 small falsified practical speedup for the naive same-weight early-exit mechanism; this is not a full validation across models or optimized serving kernels.

## Recommended next action

Stop this exact zero-training same-weight early-exit draft path; only pursue a bounded adjacent test that trains or distills lightweight exit heads and reruns the same exact-verification speed/acceptance harness.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Trained early-exit heads for exact self-speculative decoding
- Success threshold: At least 1.10x measured end-to-end speedup versus greedy full-model decoding with exact output equivalence, plus draft-token acceptance above 65% for a depth no later than 10/12 on held-out prompts.
- Stop condition: Stop if trained exits remain below 1.0x measured speedup or below 50% draft-token acceptance after a small held-out GPT-2-scale run.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-draft-on-same-weights-9c33ca2db5d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
