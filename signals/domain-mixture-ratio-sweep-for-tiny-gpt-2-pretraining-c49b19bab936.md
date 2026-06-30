# Domain mixture ratio sweep for tiny GPT-2 pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-mixture-ratio-sweep-for-tiny-gpt-2-pretraining-c49b19bab936`
Run ID: `domain-mixture-ratio-sweep-for-tiny-gpt-2-pretraining-c49b19bab936-20260621T084956606540+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/094f0ceaee0d

## What looked useful

Balanced validation favored the 50/50 mixture with mean balanced loss 2.2570 versus 2.3218 at 25/75, 2.3724 at 75/25, 10.4075 at 0/100, and 9.6551 at 100/0. Single-domain training fit the present domain but failed on the absent domain.

## Boundaries and scale limits

Synthetic domains only; 2-layer 96-wide decoder, 22.1M total training tokens across all sweep runs, 3 seeds per ratio, short local GB10 run. Does not validate natural-language/code corpora, tokenizer effects, GPT-2-small-class scale, long training, or web-scale mixture optimization.

## Claim scope

In a synthetic two-domain tiny GPT-2-style causal LM pretraining sweep with fixed token budget, the domain mixture ratio materially changed per-domain and balanced held-out loss; a 50/50 mix gave the best balanced validation loss among ratios [0, 0.25, 0.5, 0.75, 1] across 3 seeds.

## Why it stopped

Completed a bounded synthetic proxy sweep with a useful mechanism signal, but the result is not direct or broad enough for a paper.

## Recommended next action

Run a bounded deepen follow-up on two real small corpora with a tokenizer and the same ratio grid to test whether the synthetic balanced-loss optimum and per-domain tradeoff persist under direct data.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny GPT-2 domain mixture ratio sweep
- Success threshold: An interior mixture ratio improves mean balanced validation loss by at least 3% over both single-domain extremes and the result is directionally consistent across at least 2 of 3 seeds.
- Stop condition: Stop if all interior mixtures fail to improve balanced validation loss over both single-domain extremes, or if runtime/memory exceeds a documented local budget before completing at least 3 ratios.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mixture-ratio-sweep-for-tiny-gpt-2-pretraining-c49b19bab936`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
