# KV-Cache 2-Bit with Residual Scales

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-2-bit-with-residual-scales-12d65e99be62`
Run ID: `kv-cache-2-bit-with-residual-scales-12d65e99be62-20260528T143853298598+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/125b33f851bb

## What looked useful

Residual norm scales reduced output NMSE by about 38% on normal/correlated synthetic tensors, but heavy-tail output NMSE worsened by about 3% and residual-scale 2-bit remained roughly 16x to 35x worse than 4-bit output NMSE depending on distribution.

## Boundaries and scale limits

No real LLM traces, perplexity, generation quality, packed kernels, latency, or long-context serving were tested. Shapes were heads=8, seq_len=1024, head_dim=64, five seeds, CPU-only synthetic distributions.

## Claim scope

In a NumPy synthetic KV-cache proxy with grouped symmetric quantization, adding one residual norm scale per token/head vector improves 2-bit attention-error metrics on normal and correlated tensors but does not make 2-bit competitive with a 4-bit baseline and can worsen heavy-tail output error.

## Why it stopped

Proxy evidence is mixed and insufficient for a paper: the tested residual norm-scale mechanism helps some synthetic regimes but fails heavy-tail robustness and remains far behind 4-bit.

## Recommended next action

Run a bounded real-model KV-trace follow-up on a small transformer and test whether residual scales combined with outlier-aware or direction-preserving 2-bit quantization closes the gap to 4-bit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer KV traces for residual-scale 2-bit quantization
- Success threshold: Residual-scale 2-bit variant achieves less than 2x the 4-bit attention-output NMSE and less than 5% relative next-token loss degradation versus unquantized on the sampled prompts, without heavy-tail regressions.
- Stop condition: Stop if real KV traces reproduce the synthetic gap, with residual-scale 2-bit more than 5x worse than 4-bit output NMSE or any consistent perplexity regression beyond the success threshold.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-2-bit-with-residual-scales-12d65e99be62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
