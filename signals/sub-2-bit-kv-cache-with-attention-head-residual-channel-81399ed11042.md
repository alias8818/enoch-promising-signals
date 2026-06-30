# Sub-2-bit KV cache with attention-head residual channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-2-bit-kv-cache-with-attention-head-residual-channel-81399ed11042`
Run ID: `sub-2-bit-kv-cache-with-attention-head-residual-channel-81399ed11042-20260628T023622164741+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7886b0a92084

## What looked useful

At head_dim=64, 1bit+fp16_resid2 uses 1.469 payload bits/value. On synthetic head_outlier tensors across kv_len 256/1024/4096 and 5 seeds, it reduced output NRMSE from 0.9962 to 0.4800 and attention KL from 4.4587 to 0.0721 versus plain 1-bit, with 1.0 outlier-channel hit rate. On Gaussian tensors, the same variant improved NRMSE only 1.1% and KL 3.3%; on generic heavy-tail tensors it improved NRMSE 0.7% and KL 2.4%.

## Boundaries and scale limits

No trained model, real activation trace, perplexity, end-to-end generation, or optimized cache kernel was tested. Effective-bit accounting is payload-only and excludes scales/metadata. The 2-bit baseline is a simple per-vector symmetric 4-level quantizer, not a tuned production quantizer.

## Claim scope

Bounded synthetic CUDA attention-fidelity probe: preserving two high-energy FP16 residual dimensions per attention head while 1-bit quantizing the rest of K/V can substantially reduce attention error when each head has coherent outlier channels. The same mechanism showed negligible benefit on isotropic Gaussian and generic heavy-tail synthetic tensors.

## Why it stopped

The result is a synthetic attention-fidelity mechanism probe, not direct model-quality or serving evidence. It supports the residual-channel idea only under head-outlier conditions and early-falsifies a broad claim that residual channels generally rescue sub-2-bit KV cache quality.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is to test the same residual-channel selection on real transformer K/V activation traces and compare against tuned 2-bit and KIVI-style baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation sub-2-bit KV residual-channel probe
- Success threshold: At <=1.5 payload bits/value plus explicitly reported metadata, residual-channel KV quantization improves attention-output NRMSE by at least 25% versus plain 1-bit and matches or beats a tuned 2-bit baseline on KL or downstream logit/perplexity degradation for real activation traces.
- Stop condition: Stop if real activation traces do not have stable per-head outlier channels, if residual selection fails to beat plain 1-bit by 10% NRMSE, or if metadata makes the true storage budget effectively >=2 bits/value.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-kv-cache-with-attention-head-residual-channel-81399ed11042`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
