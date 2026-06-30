# Tiny-Transformer direct validation of influence-proxy shard selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-transformer-direct-validation-of-influence-proxy-shar-932a6bde2c`
Run ID: `tiny-transformer-direct-validation-of-influence-proxy-shar-932a6bde2c-20260619T061831784175+0000`

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

- Parent run decision: Influence-proxy shard selection for GPT-2-small pretraining on CPU: enoch://control-plane/projects/influence-proxy-shard-selection-for-gpt-2-small-pretraining-on-cpu-b40dd659a00d/runs/influence-proxy-shard-selection-for-gpt-2-small-pretraining-on-cpu-b40dd659a00d-20260619T060231867443+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ccc5d030cabd

## What looked useful

The gradient-dot influence proxy selected aligned shards perfectly in all 3 seeds and direct finetuning on those shards reduced held-out target loss by 34.0% versus random-k mean, with top-k loss lower than bottom-k in every seed.

## Boundaries and scale limits

Synthetic Markov-style token sequences only; tiny CPU transformer only; 3 seeds; no natural text corpus, GPT-2-small-class baseline, large shard pool, or long-horizon training.

## Claim scope

Controlled synthetic tiny-transformer sequence-modeling task with 18 shards, 3 seeds, and direct held-out target-loss evaluation after finetuning top-k, bottom-k, oracle, and random shard selections.

## Why it stopped

Tier 1 controlled direct test completed and produced a useful mechanism signal, but the evidence is synthetic and small, so it is no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up on a small natural-text or algorithmic-mixture corpus with a GPT-2-small-class or parameter-matched baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-corpus tiny-transformer validation of influence-proxy shard selection
- Success threshold: Influence top-k must beat random-k mean by at least 2% held-out target loss, beat bottom-k in at least 80% of seeds, and show no worse than 1 seed with degraded target loss versus the pretrained base.
- Stop condition: Stop if influence top-k fails to beat random-k mean by 2% in 3 of the first 5 seeds or if selection precision collapses to random when shard labels are known.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-direct-validation-of-influence-proxy-shar-932a6bde2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
