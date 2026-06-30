# Randomized-anchor RoPE scaling benchmark for tiny pretrained LMs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `randomized-anchor-rope-scaling-benchmark-for-tiny-pretrain-37088cd270`
Run ID: `randomized-anchor-rope-scaling-benchmark-for-tiny-pretrain-37088cd270-20260613T081122021552+0000`

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

- Parent run decision: RoPE Scaling for Tiny Models: Which Method Preserves Anchor Recall at 8k-16k?: enoch://control-plane/projects/rope-scaling-for-tiny-models-which-method-preserves-anchor-recall-at-8k-16k-ec8b132d0e0a/runs/rope-scaling-for-tiny-models-which-method-preserves-anchor-recall-at-8k-16k-ec8b132d0e0a-20260613T073930518640+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/db5f0839bd52

## What looked useful

Random anchors exactly tied deterministic linear and midpoint anchors in both models, while all factor-2 compressed RoPE maps were much worse than native extrapolated positions. A diagnostic confirmed position IDs are active and that shifted-anchor scaling is invariant in this setup.

## Boundaries and scale limits

Two tiny pretrained GPT-NeoX/Pythia RoPE LMs, 4 chunks per model, WikiText-2 only, no training or fine-tuning, no larger model or retrieval/task benchmark.

## Claim scope

Inference-only randomized-anchor RoPE coordinate remapping did not improve next-token NLL over deterministic origin-linear scaling on 4096-token WikiText-2 chunks for EleutherAI/pythia-14m and EleutherAI/pythia-70m.

## Why it stopped

Controlled small direct test failed the Tier 1 threshold: randomized anchors improved NLL over linear-origin scaling by 0.000000 rather than the predeclared 0.05 margin, and compressed scaling was substantially worse than native extrapolation.

## Recommended next action

Stop this inference-only branch; only pursue a bounded deepen follow-up if it trains or fine-tunes a tiny RoPE LM with randomized-anchor exposure and compares against deterministic RoPE-scaling controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny RoPE LM adaptation with randomized-anchor exposure
- Success threshold: Randomized-anchor adaptation reduces mean NLL by at least 0.05 versus deterministic linear-scaling adaptation on both pythia-14m-class and pythia-70m-class tests without worsening native extrapolation by more than 0.02 NLL.
- Stop condition: Stop if inference-only equivalence persists after adaptation or if randomized-anchor adaptation fails to beat deterministic linear scaling by 0.05 NLL on the first two completed seeds.

## Evidence references

- Artifact root: `<local-path>/projects/randomized-anchor-rope-scaling-benchmark-for-tiny-pretrain-37088cd270`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
