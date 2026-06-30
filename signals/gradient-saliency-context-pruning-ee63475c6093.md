# Gradient Saliency Context Pruning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-saliency-context-pruning-ee63475c6093`
Run ID: `gradient-saliency-context-pruning-ee63475c6093-20260608T031932282865+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de208cd5fa47

## What looked useful

Gradient saliency consistently beat random and attention controls by paired win rate, but recency matched or exceeded it in both bounded confirmations, especially at 50% and 75% pruning.

## Boundaries and scale limits

Evidence is limited to one small pretrained causal LM, 64 examples per confirmation run, short contexts up to 192 tokens, and NLL preservation only; it does not validate long-context tasks, larger models, retrieval settings, latency savings, or production KV-cache behavior.

## Claim scope

On distilgpt2 tail-token NLL preservation with prefix-only pruning at sequence/prefix lengths 128/96 and 192/160, gradient saliency improves over random and attention controls but does not beat simple recency pruning as a standalone context pruning policy.

## Why it stopped

Proxy-scale direct tests falsify the standalone superiority claim against a stronger recency baseline; this is an early bounded falsification, not a full large-model validation.

## Recommended next action

Stop this standalone gradient-saliency pruning claim as no-paper evidence; if continuing, test a recency-aware gradient hybrid against pure recency with the same NLL protocol plus one downstream long-context task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recency-Aware Gradient Saliency Hybrid Pruning
- Success threshold: A hybrid must beat pure recency by at least 0.05 mean tail-NLL delta at 50% and 75% pruning on both models and avoid downstream task accuracy loss greater than 1 percentage point versus unpruned context.
- Stop condition: Stop if hybrids fail to beat pure recency on mean tail-NLL delta at either 50% or 75% pruning on the first additional GPT-2-small-class model.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-saliency-context-pruning-ee63475c6093`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
