# Middle-surprise filtering for tiny neural LM pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `middle-surprise-filtering-for-tiny-neural-lm-pretraining-7a17cd0d86`
Run ID: `middle-surprise-filtering-for-tiny-neural-lm-pretraining-7a17cd0d86-20260520T034927445434+0000`

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

- Parent run decision: Surprise-Scored Data Pruning for Tiny Pretraining: enoch://control-plane/projects/surprise-scored-data-pruning-for-tiny-pretraining-8bc950c26145/runs/surprise-scored-data-pruning-for-tiny-pretraining-8bc950c26145-20260519T224323422391+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/66d2e6062b08

## What looked useful

Middle-surprise filtering reduced medium-family held-out NLL by 0.8265 absolute, 25.15% relative, versus equal-budget random across five seeds, with all per-seed deltas favoring middle surprise. The effect was target-specific: random was better on easy and mixture evaluation, and high-surprise was better on noise.

## Boundaries and scale limits

Synthetic corpus only; smoothed bigram pilot surprise; NumPy MLP causal LM with context length 4; five seeds; no real text, tokenizer, transformer, or large-scale pretraining evidence.

## Claim scope

In a controlled synthetic tiny neural causal LM setup with easy, medium-structured, and noisy sequence families, equal-budget middle-surprise filtering improved held-out medium-family next-token NLL versus equal-budget random, low-surprise, and high-surprise controls.

## Why it stopped

Tier 1 controlled direct test met the mechanism threshold, but the evidence remains synthetic and insufficient for publication readiness.

## Recommended next action

Run a bounded real-text deepen test using a tiny transformer, fixed pilot LM surprise scores, equal token budgets, and the same low/middle/high/random percentile controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text tiny transformer test of middle-surprise filtering
- Success threshold: Middle-surprise must improve final held-out validation NLL by at least 3% versus equal-budget random and beat both low-surprise and high-surprise controls in at least two of three seeds.
- Stop condition: Stop as unsupported if middle-surprise fails to beat equal-budget random on mean validation NLL, or if gains appear only from leakage, duplicate text, or a materially larger effective token budget.

## Evidence references

- Artifact root: `<local-path>/projects/middle-surprise-filtering-for-tiny-neural-lm-pretraining-7a17cd0d86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
