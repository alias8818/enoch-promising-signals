# Queue-Balanced Data Selection for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-balanced-data-selection-for-tiny-local-pretraining-890d1a9daac6`
Run ID: `queue-balanced-data-selection-for-tiny-local-pretraining-890d1a9daac6-20260607T111208477875+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a400e038d654

## What looked useful

Adaptive queue priority can over-focus on rare hard domains and harm macro and natural-weighted validation loss. Mild queue balancing appears useful mainly as a move away from the imbalanced natural stream, while static balanced sampling was the strongest local control.

## Boundaries and scale limits

Toy synthetic domains, tiny Transformer, short local run, and no real text/code corpus or downstream evaluation. This does not validate or refute queue-balanced selection for full local LLM pretraining on natural corpora.

## Claim scope

On a four-domain synthetic tiny causal-pretraining proxy with a fixed 600-step token budget and three seeds, loss-queue adaptive sampling did not beat a static balanced sampler. A milder queue setting beat the imbalanced natural stream on macro-domain validation loss but remained worse than static balanced sampling.

## Why it stopped

No-paper useful signal: the adaptive queue-balanced sampler failed against the static balanced control in the direct toy test, and the positive mild-queue result was only relative to the imbalanced natural baseline.

## Recommended next action

Stop the paper path for this synthetic result; only pursue a bounded deepen test if using a real small corpus mixture and requiring mild queue balancing to beat static balanced sampling on held-out per-domain perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny pretraining test of mild queue balancing versus static balanced sampling
- Success threshold: Mild queue-balanced sampling must reduce macro held-out perplexity by at least 2% versus static balanced sampling while keeping natural-mixture perplexity within 5% of static balanced.
- Stop condition: Stop if mild queue-balanced sampling is worse than static balanced on macro held-out perplexity in two seeds or if it improves macro perplexity only by sacrificing more than 5% natural-mixture perplexity.

## Evidence references

- Artifact root: `<local-path>/projects/queue-balanced-data-selection-for-tiny-local-pretraining-890d1a9daac6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
