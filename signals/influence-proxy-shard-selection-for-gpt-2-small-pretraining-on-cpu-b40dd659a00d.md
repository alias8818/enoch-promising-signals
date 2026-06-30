# Influence-proxy shard selection for GPT-2-small pretraining on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `influence-proxy-shard-selection-for-gpt-2-small-pretraining-on-cpu-b40dd659a00d`
Run ID: `influence-proxy-shard-selection-for-gpt-2-small-pretraining-on-cpu-b40dd659a00d-20260619T060231867443+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ccc5d030cabd

## What looked useful

Across 10 seeds, influence-proxy final test loss averaged 3.9605 versus 4.0719 for random and 4.1100 for high-train-loss selection. The influence proxy selected useful target/near-target shards in 100% of budget slots and matched the one-step validation oracle in this proxy.

## Boundaries and scale limits

NumPy bigram proxy only; no GPT-2-small architecture, tokenizer, real corpus, optimizer schedule, long-context dynamics, or full pretraining wall-clock was tested. CPU-only run completed in 24.56 seconds with 42,656 KB max RSS.

## Claim scope

In a controlled synthetic next-token bigram proxy, validation-gradient dot-product shard selection improved target held-out loss versus random and train-loss shard selection, and matched a one-step validation oracle. This does not validate GPT-2-small pretraining.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic proxy mechanism test, not direct GPT-2-small pretraining validation.

## Recommended next action

Run a bounded direct tiny-Transformer or GPT-2-small-class CPU experiment with real tokenized shards and the same influence, random, and loss baselines before making any GPT-2-small claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-Transformer direct validation of influence-proxy shard selection
- Success threshold: Influence-proxy selection reduces final held-out target loss by at least 2% versus random and high-train-loss baselines with consistent direction in at least 4 of 5 seeds.
- Stop condition: Stop if the influence proxy fails to beat random by 1% in mean held-out loss after the bounded tiny-Transformer budget, or if direct model training cannot run within the allocated CPU wall-clock.

## Evidence references

- Artifact root: `<local-path>/projects/influence-proxy-shard-selection-for-gpt-2-small-pretraining-on-cpu-b40dd659a00d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
