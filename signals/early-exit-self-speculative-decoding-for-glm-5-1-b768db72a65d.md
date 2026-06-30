# Early-exit self-speculative decoding for GLM-5.1

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-self-speculative-decoding-for-glm-5-1-b768db72a65d`
Run ID: `early-exit-self-speculative-decoding-for-glm-5-1-b768db72a65d-20260531T155352753797+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cb6a73846e0f

## What looked useful

Corrected runs found best speedup proxy 0.690x for DistilGPT-2 and 0.769x for GPT-2-small; all tested exits and gamma values were slower than the final-layer greedy baseline. The simple no-training early-exit drafter is therefore not worth scaling directly to GLM-5.1 without first improving exit calibration.

## Boundaries and scale limits

No GLM-5.1 weights or intermediate activations were run. The test used 24 prompts x 32 generated tokens per model on two GPT-style dense proxies, not GLM-5.1 MoE/DSA routing, long-context workloads, or production serving kernels.

## Claim scope

Small-model proxy evidence for untrained/tied-head early-exit self-speculative decoding: on DistilGPT-2 and GPT-2-small, intermediate hidden states with final layer norm plus tied LM head did not produce enough accepted draft tokens to beat greedy decoding under a conservative layer-latency proxy.

## Why it stopped

Early proxy falsification, not full GLM-5.1 validation: two corrected small causal-LM probes showed no speedup setting, with best observed speed proxy below baseline at 0.769x.

## Recommended next action

Stop this no-training early-exit variant; only continue with a bounded follow-up that trains or calibrates lightweight exit heads and requires a held-out speed proxy above 1.10x before any GLM-5.1-scale work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated early-exit heads for self-speculative decoding on small causal LMs
- Success threshold: Held-out gamma 2 speedup_proxy >= 1.10 at an exit depth <=25% with no worse than 1% token mismatch versus verified greedy output.
- Stop condition: Stop if calibrated exits at <=25% depth remain below 1.00x speed proxy or require exits deeper than 50% to reach useful acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-for-glm-5-1-b768db72a65d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
