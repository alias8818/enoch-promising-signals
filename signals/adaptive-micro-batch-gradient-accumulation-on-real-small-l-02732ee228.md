# Adaptive Micro-batch Gradient Accumulation on Real Small-LM Fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-micro-batch-gradient-accumulation-on-real-small-l-02732ee228`
Run ID: `adaptive-micro-batch-gradient-accumulation-on-real-small-l-02732ee228-20260524T021323841800+0000`

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

- Parent run decision: Micro-batch VRAM-Adaptive Gradient Accumulation for Home Training: enoch://control-plane/projects/micro-batch-vram-adaptive-gradient-accumulation-for-home-training-0ea10ae9d6c9/runs/micro-batch-vram-adaptive-gradient-accumulation-for-home-training-0ea10ae9d6c9-20260524T005309940394+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d71a8a620cd6

## What looked useful

Counterbalanced direct testing found no robust throughput gain for naive adaptive accumulation: adaptive/fixed tokens/sec was 1.0218 when fixed ran first but 0.9727 when adaptive ran first, mean 0.9973. Adaptive did not reduce padding waste (padding multiplier ratio 1.0017). Lower eval loss is confounded by adaptive taking 52 optimizer steps versus 47 fixed steps at similar token budget.

## Boundaries and scale limits

Single corpus, single seed, approximately 120k training tokens per condition, distilgpt2 only, no length bucketing, no hyperparameter sweep, and no 7B-class or multi-node validation.

## Claim scope

Tier 1 controlled small direct test of naive adaptive micro-batch gradient accumulation versus fixed accumulation for distilgpt2 fine-tuning on variable-length Tiny Shakespeare token sequences on GB10 CUDA.

## Why it stopped

Naive adaptive accumulation failed the Tier 1 efficiency signal under counterbalanced direct testing; this is a no-paper useful signal rather than full validation.

## Recommended next action

Run one bounded deepen test with matched token budget and matched optimizer-update count using a length-bucketed adaptive micro-batch scheduler; stop if it fails to reduce padding by at least 10 percent and improve tokens/sec by at least 5 percent without eval-loss regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-bucketed adaptive micro-batch accumulation with matched update count
- Success threshold: Length-bucketed adaptive accumulation reduces padding multiplier by at least 10 percent and improves real tokens/sec by at least 5 percent versus fixed accumulation, with no final eval-loss regression greater than 0.02, in at least two of three seeds.
- Stop condition: Stop if the first two matched-update seeds show less than 3 percent throughput improvement or any consistent eval-loss regression above 0.02, because the mechanism is unlikely to justify further local testing.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-micro-batch-gradient-accumulation-on-real-small-l-02732ee228`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
