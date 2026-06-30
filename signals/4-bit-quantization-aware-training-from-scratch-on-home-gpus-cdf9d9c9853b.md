# 4-bit quantization-aware training from scratch on home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantization-aware-training-from-scratch-on-home-gpus-cdf9d9c9853b`
Run ID: `4-bit-quantization-aware-training-from-scratch-on-home-gpus-cdf9d9c9853b-20260527T221221032882+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0baf61e57fbd

## What looked useful

Small controlled GB10 runs show 4-bit QAT from scratch is not immediately falsified: W4 and W4A4 met the predefined mean local viability threshold, but seed-level deltas were mixed and the implementation does not prove memory savings.

## Boundaries and scale limits

Synthetic task only; 3 seeds; 3000 steps; fake-quant QAT with fp32 master weights, not packed 4-bit kernels or optimizer-state memory reduction; no natural-language corpus, GPT-2-small-class scale, long-run stability, or full pretraining validation.

## Claim scope

On a GB10 home GPU, a 618k-parameter causal transformer trained from scratch on a synthetic affine-recurrence next-token task can use straight-through 4-bit fake-quant QAT without mean validation loss degradation versus dense over three seeds; W4 averaged +0.019 loss delta at 0.94x throughput and W4A4 averaged +0.014 loss delta at 0.57x throughput.

## Why it stopped

No paper now: evidence is useful but limited to a small synthetic proxy and mixed seed-level outcomes, not full validation of 4-bit QAT from scratch.

## Recommended next action

Run a bounded real-corpus deepen test on WikiText-2 or TinyStories with a parameter-matched small transformer, at least five seeds or data shards, and the same dense/W4/W4A4 controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus small-transformer validation of 4-bit QAT from scratch
- Success threshold: Mean held-out loss delta for at least one 4-bit variant is <= 0.20 versus dense, no catastrophic seed fails, and throughput is >= 0.35x dense under the same training budget.
- Stop condition: Stop if both 4-bit variants exceed +0.30 held-out loss delta versus dense on at least three seeds or throughput falls below 0.35x dense without a compensating accuracy signal.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantization-aware-training-from-scratch-on-home-gpus-cdf9d9c9853b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
