# 1-bit KV with Residual Channel Recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-kv-with-residual-channel-recovery-6f0a47a723e5`
Run ID: `1-bit-kv-with-residual-channel-recovery-6f0a47a723e5-20260527T205643828648+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c64e4140781c

## What looked useful

Top residual channel recovery is a real local mechanism signal: r=4 per 64-d head at 1.94 effective bits/scalar reduced mean attention-output relative MSE from 0.5634 to 0.5165, while random r=4 averaged 0.5417; r=8 reduced it to 0.4635 versus random 0.5169. Absolute distortion remains high and attention top-1 agreement remains much lower than a simple 2-bit reference.

## Boundaries and scale limits

No packed KV kernel, no autoregressive generation loop, no perplexity benchmark, no latency or real memory-bandwidth measurement, one small GPT-2-class model and short fixed text only.

## Claim scope

Activation-level probe on distilgpt2 Q/K/V tensors over 384 tokens and 6 layers: top residual FP16 channels added to 1-bit KV reduce attention-output relative MSE versus plain 1-bit and random residual controls.

## Why it stopped

Proxy activation-level evidence supports the mechanism but is insufficient for a paper or production claim; direct end-to-end cache evidence is still missing.

## Recommended next action

Stop this run as a no-paper useful signal; next run should implement an autoregressive residual-channel KV cache and compare logit KL/perplexity drift plus memory against int2/int4 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end residual-channel 1-bit KV cache perplexity probe
- Success threshold: Residual-channel 1-bit at <=2.0 effective bits/scalar improves logit KL or perplexity drift by at least 20% over plain 1-bit, beats random residual controls, and is no worse than a 2-bit baseline on the primary quality metric.
- Stop condition: Stop if residual-channel 1-bit fails to beat random residual controls or remains worse than the 2-bit baseline at comparable effective memory on two prompt/text slices.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-kv-with-residual-channel-recovery-6f0a47a723e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
