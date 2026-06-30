# Held-out end-to-end GPT-2 KV residual decode test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `held-out-end-to-end-gpt-2-kv-residual-decode-test-0adb2a0ea3`
Run ID: `held-out-end-to-end-gpt-2-kv-residual-decode-test-0adb2a0ea3-20260523T192913400832+0000`

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

- Parent run decision: Quantized KV Cache with Per-Head Residual Channels: enoch://control-plane/projects/quantized-kv-cache-with-per-head-residual-channels-007da086960e/runs/quantized-kv-cache-with-per-head-residual-channels-007da086960e-20260523T190843160160+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/00855c71463b

## What looked useful

Across two seeds, full-KV ridge decoders achieved held-out NLL 4.65 and 4.72 versus true GPT-2 NLL 4.43 and 4.53, recovering about 93% of the mean-hidden/bias-only to true-GPT-2 NLL gap. Shuffled KV controls collapsed to NLL about 10.86-10.87, supporting that aligned KV activations carry residual-decodable signal.

## Boundaries and scale limits

Tested only GPT-2 small on one small public corpus with 4096 train and 1024 validation token positions per seed. The probe reconstructs same-token final hidden states and does not validate cache-only serving, compression, larger models, broader corpora, causal mechanisms, or paper-grade robustness.

## Claim scope

In a Tier 1 controlled small direct test on pretrained GPT-2 and a held-out Tiny Shakespeare split, linear probes from same-token KV-cache activations can reconstruct enough final hidden-state information to preserve most next-token predictive performance through the frozen GPT-2 LM head.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is not paper-positive because it is small-corpus, same-token, and lacks broader model/corpus robustness or causal/deployment ablations.

## Recommended next action

Run a bounded deepen test on WikiText or OpenWebText-style held-out data with GPT-2 small plus a second GPT-2-class model, layer/token ablations, and a predeclared success threshold for NLL-gap recovery versus shuffled and mean-hidden controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-corpus GPT-2 KV residual decode robustness test
- Success threshold: Full-KV or value-only decoders recover at least 80% of the bias-only to true-GPT-2 NLL gap on each corpus/model setting, with shuffled KV no better than the mean-hidden control and top-5 within 10 percentage points of the true hidden-state decode.
- Stop condition: Stop as unsupported if NLL-gap recovery falls below 50% on broader held-out corpora or if shuffled controls approach the real-KV decoder, indicating corpus prior or leakage rather than aligned KV signal.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-end-to-end-gpt-2-kv-residual-decode-test-0adb2a0ea3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
