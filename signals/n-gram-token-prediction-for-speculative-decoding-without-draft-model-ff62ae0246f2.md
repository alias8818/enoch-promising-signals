# N-gram Token Prediction for Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-token-prediction-for-speculative-decoding-without-draft-model-ff62ae0246f2`
Run ID: `n-gram-token-prediction-for-speculative-decoding-without-draft-model-ff62ae0246f2-20260612T024841293920+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d9a379bc68fa

## What looked useful

Full-history n-gram proposals can exploit target-model repetition and materially reduce idealized verifier calls in a bounded GPT-2-small trace, but the signal largely collapses on less repetitive natural-text continuations. This suggests draft-free n-gram speculation is workload-sensitive and should be treated as a repetition/local-copy accelerator, not a broad draft-model replacement based on current evidence.

## Boundaries and scale limits

No end-to-end speculative decoding latency was measured; only GPT-2-small greedy traces were directly tested; no larger target models, sampling regimes, code workloads, batched verifier passes, or KV-cache effects were evaluated. The strongest direct signal is confounded by highly repetitive target-model continuations.

## Claim scope

On GPT-2-small greedy continuations from War and Peace prompt chunks, a full-history n-gram proposer without a draft model can predict repeated local spans and reached 1.365 accepted tokens per verifier call at gamma 8 in an offline exact-match probe. The same mechanism was much weaker on next-corpus-token continuations, reaching 0.139 accepted tokens per call at gamma 8.

## Why it stopped

Bounded offline evidence is mixed: direct GPT-2-small greedy traces support the mechanism under high repetition, while the corpus-control proxy early-falsifies a broad claim that n-gram proposals generally predict future tokens well without a draft model.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement real verifier-block speculative decoding and measure wall-clock latency on two small or medium target models across repetitive and non-repetitive workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end latency test for full-history n-gram speculative decoding
- Success threshold: At least 10% end-to-end tokens/s improvement over greedy decoding on a repetitive/local-copy workload with no output divergence, while showing less than 3% regression on ordinary prose.
- Stop condition: Stop if verifier-block overhead eliminates speedup on the repetitive workload or if accepted tokens per call remains below 0.25 on both workload classes.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-token-prediction-for-speculative-decoding-without-draft-model-ff62ae0246f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
