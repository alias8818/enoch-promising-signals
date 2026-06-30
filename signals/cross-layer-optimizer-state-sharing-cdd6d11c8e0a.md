# Cross-Layer Optimizer State Sharing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-optimizer-state-sharing-cdd6d11c8e0a`
Run ID: `cross-layer-optimizer-state-sharing-cdd6d11c8e0a-20260621T104642227966+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/e2df2029c8a7

## What looked useful

Cross-layer sharing of only Adam's second moment is a plausible memory-saving mechanism worth testing in transformer language modeling; aggressive sharing of both Adam moments showed a clear convergence penalty on this bounded proxy.

## Boundaries and scale limits

Synthetic residual MLP only; no transformer language modeling, no GPT-2-small-class baseline, no mixed precision, no distributed optimizer sharding, and no production fused optimizer implementation. Wall-clock speed is not claimed because the custom Python optimizer is slower than standard AdamW.

## Claim scope

On a 3-seed synthetic teacher-regression residual-MLP proxy, sharing AdamW second-moment state across repeated layers preserved validation loss within 0.24% of AdamW while reducing optimizer-state memory to 55.1%; sharing both first and second moments reduced state memory to 10.2% but worsened validation loss by 43.9%.

## Why it stopped

No-paper closure: local evidence is a synthetic proxy useful signal, not direct publication-grade validation of cross-layer optimizer state sharing for transformers or LLMs.

## Recommended next action

Run a bounded tiny-transformer language-model follow-up comparing AdamW, shared_v, and shared_mv at matched parameter count with validation perplexity and optimizer-state memory as primary metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Test of Shared Adam Second Moments
- Success threshold: shared_v reaches validation loss/perplexity within 1% of AdamW across at least 3 seeds while using at most 65% of AdamW optimizer-state memory.
- Stop condition: Stop if shared_v is worse than AdamW by more than 3% validation loss/perplexity after the same token budget or if Python optimizer overhead prevents a fair bounded run without implementing lower-level optimizer support.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-optimizer-state-sharing-cdd6d11c8e0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
