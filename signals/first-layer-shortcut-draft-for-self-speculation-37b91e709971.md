# First-Layer Shortcut Draft for Self-Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `first-layer-shortcut-draft-for-self-speculation-37b91e709971`
Run ID: `first-layer-shortcut-draft-for-self-speculation-37b91e709971-20260603T234213952495+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9b0f2019f36a

## What looked useful

First-layer hidden states carry a reproducible shortcut signal for the full model's final greedy token: tied layer-1 acceptance was about 19.0%, and 720 shortcut-head training steps raised it to 34.6%, versus 18.2% for a trained embedding-layer control. This supports mechanism exploration but not a practical self-speculation claim.

## Boundaries and scale limits

Single small pretrained model, one dataset split, 24,576 held-out token positions, no real speculative decoding loop, no wall-clock decoding speedup measurement, no low-rank/cost-reduced head, and no robustness across larger models or domains.

## Claim scope

On frozen distilgpt2 over WikiText-2 blocks, a first-transformer-block shortcut head initialized from the tied LM head and trained to imitate full-model greedy next-token choices reached 34.6% held-out greedy-token acceptance, outperforming embedding-layer controls under the same protocol.

## Why it stopped

Bounded proxy evidence supports a first-layer shortcut mechanism, but acceptance is only 34.6% and no direct decoding speedup was measured, so the practical self-speculation hypothesis remains mixed rather than paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should implement actual verified multi-token speculative decoding with latency accounting for the trained first-layer shortcut.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verified Multi-Token First-Layer Shortcut Decoding
- Success threshold: At least 1.10x wall-clock decoding speedup over full greedy decoding on a held-out prompt set with exact output equivalence under greedy verification and no more than a 5% increase in peak memory.
- Stop condition: Stop as negative if verified decoding is slower than full greedy decoding or if acceptance remains below 45% after a bounded shortcut training budget.

## Evidence references

- Artifact root: `<local-path>/projects/first-layer-shortcut-draft-for-self-speculation-37b91e709971`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
