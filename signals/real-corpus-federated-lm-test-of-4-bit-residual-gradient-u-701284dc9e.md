# Real-Corpus Federated LM Test of 4-bit Residual Gradient Uplink Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-corpus-federated-lm-test-of-4-bit-residual-gradient-u-701284dc9e`
Run ID: `real-corpus-federated-lm-test-of-4-bit-residual-gradient-u-701284dc9e-20260527T123811539362+0000`

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

- Parent run decision: Quantized Residual Gradients for Home Federated Pretraining: enoch://control-plane/projects/quantized-residual-gradients-for-home-federated-pretraining-5a9f4d73fe71/runs/quantized-residual-gradients-for-home-federated-pretraining-5a9f4d73fe71-20260527T104621287955+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9544abdcc655

## What looked useful

Residual/error-feedback was the decisive mechanism: 4-bit residual averaged -0.0229 nats/token delta versus dense at 8.00x compression, while 4-bit without residual averaged +0.2208 nats/token and failed the tolerance in every seed.

## Boundaries and scale limits

Three seeds, 60 rounds, 8 simulated clients, 4 clients per round, synchronous FedSGD-style updates, character-level GRU, WikiText-2 only. Not tested on transformer/subword LMs, larger corpora, Adam-style optimizer states, real cross-device networks, privacy constraints, or long convergence.

## Claim scope

In a small local federated simulation on WikiText-2 with a tiny character GRU language model, 4-bit symmetric gradient uplink quantization with client-side residual/error feedback matched dense FP32 validation loss within the predeclared Tier-1 tolerance while reducing uplink bits by about 8x.

## Why it stopped

Tier-1 direct evidence supports the mechanism but is too small and model-specific for publication readiness; close this worker run as no-paper useful signal rather than overclaiming.

## Recommended next action

Run a bounded medium confirmation with a tiny transformer or GPT-2-small-class subword LM, non-IID client partitions, repeated seeds, and the same dense versus 4-bit residual versus no-residual controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Real-Corpus Transformer Federated LM Test of 4-bit Residual Uplinks
- Success threshold: 4-bit residual final validation loss is within +0.10 nats/token or +5% relative of dense in at least three seeds while uplink bits are at least 7.5x lower; no-residual should be worse or otherwise explain why residuals are unnecessary.
- Stop condition: Stop as unsupported if 4-bit residual exceeds both the +0.10 nats/token and +5% degradation thresholds in two or more seeds, or if the communication reduction falls below 7.5x.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-federated-lm-test-of-4-bit-residual-gradient-u-701284dc9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
