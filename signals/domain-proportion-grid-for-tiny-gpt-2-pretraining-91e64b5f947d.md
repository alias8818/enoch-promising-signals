# Domain Proportion Grid for Tiny GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-proportion-grid-for-tiny-gpt-2-pretraining-91e64b5f947d`
Run ID: `domain-proportion-grid-for-tiny-gpt-2-pretraining-91e64b5f947d-20260628T214941813519+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4581481eb0d4

## What looked useful

The grid exposed stable domain tradeoffs: the best interior mixture had 1.6812 mean balanced validation loss, while the best pure-domain mixture had 3.3961, a 1.7149 nats/token gap. Exact best interior ratio varied by seed, so only the interior-mixture mechanism is supported.

## Boundaries and scale limits

Tiny 2-layer transformer, synthetic domains, character tokens, 80 train steps per grid cell, no natural corpora, no full Tiny GPT-2/BPE training, and no downstream transfer evaluation.

## Claim scope

In a CPU-bounded synthetic character-level GPT-style LM probe with three domains, 15 mixture grid cells, and three seeds, interior domain mixtures produced much lower balanced held-out next-token loss than pure-domain pretraining.

## Why it stopped

Local evidence is direct for a toy GPT-style LM but only proxies the full Tiny GPT-2 pretraining claim, so it is not publication-grade validation.

## Recommended next action

Stop as no-paper useful signal; next concrete test is a bounded natural-corpus Tiny GPT-2-class repeat with BPE tokenization and the same 15-cell domain grid.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus Tiny GPT-2-class domain grid
- Success threshold: Best interior mixture improves balanced validation loss over the best pure-domain mixture by at least 0.10 nats/token and preserves the effect in at least two of three seeds.
- Stop condition: Stop if no interior mixture beats the best pure-domain baseline by 0.05 nats/token after the planned token budget, or if CPU-only runtime exceeds the deployment budget without GPU access.

## Evidence references

- Artifact root: `<local-path>/projects/domain-proportion-grid-for-tiny-gpt-2-pretraining-91e64b5f947d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
