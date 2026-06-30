# Draft-only early exits on GPT-2-small self-speculative decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `draft-only-early-exits-on-gpt-2-small-self-speculative-dec-633c68e4a2`
Run ID: `draft-only-early-exits-on-gpt-2-small-self-speculative-dec-633c68e4a2-20260608T181955709708+0000`

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

- Parent run decision: Self-Speculative Decoding with Draft-Only Early Exit Layers: enoch://control-plane/projects/self-speculative-decoding-with-draft-only-early-exit-layers-3622720c4b7e/runs/self-speculative-decoding-with-draft-only-early-exit-layers-3622720c4b7e-20260608T154153550420+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/75bbb8f75b39

## What looked useful

Cheap exits failed by acceptance quality: layer 8 with draft length 4 had only 0.137 accepted tokens per drafted token and 71.1% zero-accept cycles despite an ideal block-work ratio below 1.0. Later layers accepted more tokens but had ideal block-work ratios at or above full greedy decoding.

## Boundaries and scale limits

Small controlled direct test only: GPT-2-small, 128 prompt windows, greedy verification, no optimized serving implementation, no trained auxiliary exit heads, no broad-corpus robustness study, and no wall-clock production decoder benchmark.

## Claim scope

On GPT-2-small greedy decoding over 128 Wikitext-2 validation prompt windows, draft-only intermediate exits formed by applying the final layer norm and tied LM head to hidden states did not produce enough accepted draft tokens for practical self-speculative decoding.

## Why it stopped

Direct Tier 1 plus 128-prompt confirmation falsified the draft-only acceptance threshold rather than providing publication-grade support.

## Recommended next action

Stop this draft-only branch; only branch if changing the hypothesis to trained or calibrated auxiliary exit heads with a direct acceptance threshold.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Train lightweight GPT-2-small exit heads for self-speculative drafts
- Success threshold: Layer 8 or earlier, draft length 4, held-out accepted_per_draft_token >= 0.50, zero_accept_rate <= 0.35, and ideal_block_work_ratio_vs_full_greedy < 1.0.
- Stop condition: Stop if trained/calibrated layer 8 or earlier remains below 0.35 accepted_per_draft_token on held-out prompts or requires layer 10 or later to reach useful acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/draft-only-early-exits-on-gpt-2-small-self-speculative-dec-633c68e4a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
