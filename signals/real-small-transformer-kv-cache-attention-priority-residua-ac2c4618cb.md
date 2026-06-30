# Real Small-Transformer KV-Cache Attention-Priority Residual Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-small-transformer-kv-cache-attention-priority-residua-ac2c4618cb`
Run ID: `real-small-transformer-kv-cache-attention-priority-residua-ac2c4618cb-20260531T193313492680+0000`

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

- Parent run decision: Attention-Priority Asymmetric Residual Quantization: enoch://control-plane/projects/attention-priority-asymmetric-residual-quantization-323e85d544e9/runs/attention-priority-asymmetric-residual-quantization-323e85d544e9-20260531T153334964260+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/58a9b8942e46

## What looked useful

On 4,032 cached-forward perturbations, attention-priority residuals reduced mean KL by 52.2% to 61.4% versus recency and 51.5% to 59.6% versus random at equal restored-token budgets, with paired KL win rates of 81.3% to 85.4% versus recency for 10% residual and 70.8% to 81.8% versus random across tested settings.

## Boundaries and scale limits

One small pretrained GPT-style model, 12 fixed prompts, 16 greedy decode steps, simple whole-tensor simulated quantization, no packed kernels, no long-context perplexity/task benchmark, and no end-to-end serving latency or memory-bandwidth measurement.

## Claim scope

Tier-1 direct test on distilgpt2: cumulative-attention priority for exact KV-cache residual restoration reduced next-token logit-distribution distortion versus equal-budget recency and random residual selection across 2-, 3-, and 4-bit simple quantization.

## Why it stopped

Controlled small direct evidence supports the mechanism but is insufficient for a paper because it lacks larger-model replication, long-context quality metrics, and production-style packed KV-cache implementation evidence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepening should test a GPT-2-small-class model with longer contexts and perplexity/task metrics before considering packed-kernel engineering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small long-context priority KV residual quantization
- Success threshold: Priority residual selection must improve mean KL or NLL by at least 10% versus both recency and random at the same memory budget in at least four of six bit/budget settings, with paired win rate above 60%.
- Stop condition: Stop if priority fails to beat both recency and random by 10% mean KL/NLL in at least four settings or if longer-context overhead/memory accounting makes the residual policy noncompetitive.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-transformer-kv-cache-attention-priority-residua-ac2c4618cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
