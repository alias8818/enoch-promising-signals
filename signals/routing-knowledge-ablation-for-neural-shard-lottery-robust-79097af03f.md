# Routing-knowledge ablation for neural shard lottery robustness

Status: `useful_signal`
Project ID: `routing-knowledge-ablation-for-neural-shard-lottery-robust-79097af03f`
Run ID: `routing-knowledge-ablation-for-neural-shard-lottery-robust-79097af03f-20260518T221612674227+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Routing-knowledge ablation for neural shard lottery robustness: internal_generated:routing-knowledge-ablation-for-neural-shard-lottery-robust-79097af03f

## What looked useful

Shard dropout, not routing-knowledge ablation alone, was the dominant robustness intervention: ablated_plus_shard_dropout reached 0.9459 mean worst-single-drop accuracy and 0.7254 retain-one accuracy, while routing_knowledge_ablated reached 0.8002 and 0.4755 respectively.

## Boundaries and scale limits

Evidence is synthetic/local and uses small MLP experts, not GPT-2-small-class transformers, real language modeling, sparse production MoE routing, or datacenter-scale training.

## Claim scope

On a 16-seed synthetic modular classification benchmark with 6 soft MoE shards, routing-knowledge ablation with entropy balancing modestly improves some shard-lottery metrics over a routing-knowledge MoE, but it does not make the model robust and is dominated by matched shard-dropout controls.

## Why it stopped

Bounded full validation produced direct shard-lottery metrics and falsified routing-knowledge ablation as the main robustness mechanism; the positive signal belongs mainly to shard dropout and is not paper-positive in this synthetic setting.

## Recommended next action

Stop this run as no-paper evidence; if one final depth-4 follow-up is allowed, test the shard-dropout-vs-routing-ablation factorization on a small transformer language-model task with parameter-matched dense and sharded baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer shard dropout versus routing-knowledge ablation
- Success threshold: Shard-dropout variants must reduce worst-single-shard perplexity degradation by at least 50% versus routing_knowledge and beat routing_knowledge_ablated on retain-1/retain-2 metrics without more than 3% clean perplexity regression.
- Stop condition: Stop if shard dropout does not beat routing_knowledge_ablated on worst-drop and retain-subset metrics in at least 4 of 5 seeds, or if clean perplexity regresses by more than 3%.

## Evidence references

- Artifact root: `<local-path>/projects/routing-knowledge-ablation-for-neural-shard-lottery-robust-79097af03f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
