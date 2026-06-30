# Perplexity-Gated Q4/Q8 Cascade Router for Home GPUs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `perplexity-gated-q4-q8-cascade-router-for-home-gpus-351d454ac1a4`
Run ID: `perplexity-gated-q4-q8-cascade-router-for-home-gpus-351d454ac1a4-20260531T234131373878+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4b1cd1e04538

## What looked useful

Q8 stayed close to FP perplexity (+3.0%), but Q4 collapsed to 7247.7 perplexity versus FP 85.3. Q4 perplexity had negative correlation with Q8 benefit (-0.224), and routing the highest-perplexity 15.9% of tokens recovered only 17.1% of the Q4-to-Q8 NLL gap. The proxy cascade degenerates toward using Q8 almost everywhere.

## Boundaries and scale limits

Does not test true int4/int8 kernels, KV-cache behavior, generation quality, llama.cpp/exllama/vLLM backends, group-wise production quantization formats, or 1B-7B home-GPU models.

## Claim scope

Small local proxy on distilgpt2 with Wikitext-2 validation: row-wise symmetric dequantized-float Q4/Q8 weight proxies, per-sample perplexity routing, 96 samples and 7111 scored tokens on GB10.

## Why it stopped

The bounded proxy directly tested Q4-perplexity sample routing and found the selector weak with Q4 quality too poor for a useful cascade; this is not a full production validation.

## Recommended next action

Stop this run as a proxy early falsification; only revisit with a true GGUF/exllama/vLLM Q4/Q8 backend on a 1B-3B model if the goal is to test production quantization rather than this simulated-weight mechanism.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True-backend Q4/Q8 cascade probe on a 1B-3B instruction model
- Success threshold: Route <=30% of tokens or prompts to Q8, recover >=70% of the Q4-to-Q8 NLL gap, keep cascade perplexity within 10% of all-Q8, and show end-to-end latency or memory advantage versus all-Q8 on the target home GPU.
- Stop condition: Stop if production Q4 perplexity is more than 50% worse than Q8 on the validation corpus or if the learned/threshold gate correlation with Q8 benefit is below 0.3.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-gated-q4-q8-cascade-router-for-home-gpus-351d454ac1a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
