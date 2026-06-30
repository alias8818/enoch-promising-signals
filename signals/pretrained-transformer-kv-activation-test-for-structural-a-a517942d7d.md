# Pretrained Transformer KV-Activation Test for Structural Anchor Mixed Precision

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-transformer-kv-activation-test-for-structural-a-a517942d7d`
Run ID: `pretrained-transformer-kv-activation-test-for-structural-a-a517942d7d-20260602T225750997707+0000`

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

- Parent run decision: Structural Anchor Mixed-Precision KV Cache: enoch://control-plane/projects/structural-anchor-mixed-precision-kv-cache-b8c195870477/runs/structural-anchor-mixed-precision-kv-cache-b8c195870477-20260602T185730991724+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bbe37b6af998

## What looked useful

Real pretrained KV-cache evidence is mixed: structural anchors improve distilgpt2 logit L2/KL versus random but not NLL, while Pythia-14M passes the paired NLL threshold but suffers severe absolute quantization degradation. The mechanism is plausible but fixed structural anchors are not robust enough for a paper or deployment claim.

## Boundaries and scale limits

Only six deterministic text snippets, 128-token prefixes, 32 evaluated next-token steps, fake quantization rather than packed kernels, no natural held-out corpus, no GPT-2-small or larger model, no latency/throughput measurement, and no attention-mass-conditioned anchor proof.

## Claim scope

Tier 1 direct test on two small cached pretrained transformers, distilgpt2 and EleutherAI/pythia-14m, using incremental next-token evaluation with fake row-wise KV-cache quantization. Fixed punctuation/newline/document-start structural anchors sometimes reduce logit/KL drift and pass paired NLL controls on Pythia-14M, but fail the primary NLL threshold on distilgpt2.

## Why it stopped

Direct small pretrained-transformer validation produced mixed evidence: one model failed the stated NLL success threshold and the model that passed did so under severe absolute quality degradation.

## Recommended next action

Run a bounded attention-mass-conditioned GPT-2-small-class follow-up on held-out natural text; stop paper pursuit here because this Tier 1 direct test is mixed and not paper-positive.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Attention-Mass-Conditioned Structural Anchor KV Mixed Precision on GPT-2 Small
- Success threshold: Attention-mass-conditioned structural mixed precision must beat matched random and key-norm controls on mean NLL drift and KL drift, win at least 75% of paired windows, and keep top-1 agreement no worse than random at a KV footprint below 25% of fp32.
- Stop condition: Stop if measured structural anchors do not receive persistent attention mass, or if attention-conditioned structural selection fails to beat both random and key-norm controls on paired NLL in the first 128 held-out windows.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-transformer-kv-activation-test-for-structural-a-a517942d7d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
