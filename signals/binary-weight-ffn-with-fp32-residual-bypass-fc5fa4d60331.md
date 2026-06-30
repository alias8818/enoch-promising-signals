# Binary-Weight FFN with FP32 Residual Bypass

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `binary-weight-ffn-with-fp32-residual-bypass-fc5fa4d60331`
Run ID: `binary-weight-ffn-with-fp32-residual-bypass-fc5fa4d60331-20260602T224740844541+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bfc35e4763c

## What looked useful

Binary+bypass reached 0.7741 mean validation accuracy versus 0.7494 for binary-only and 0.7615 for dense; paired bypass-minus-binary accuracy improvement was +0.02466 mean and positive on all 5 seeds. Effective storage was 24,640 bytes for bypass versus 8,256 for binary-only and 135,232 for dense.

## Boundaries and scale limits

This was not a Transformer or language-model experiment; it used synthetic teacher labels, a single residual FFN block, small dimensions, no real corpus, no hardware-aware binary kernels, and no GPT-2-small-class or larger training.

## Claim scope

On a CPU-only NumPy teacher-generated residual FFN classification task, adding a zero-initialized FP32 residual bypass to a binary-weight FFN improved validation accuracy and loss versus binary-only across 5 paired seeds while retaining lower effective storage than the dense FFN baseline.

## Why it stopped

No-paper useful signal: the result is a synthetic/proxy mechanism test, not direct architecture evidence on real language modeling or deployed binary kernels.

## Recommended next action

Run a bounded tiny Transformer language-model follow-up comparing dense FFN, binary-only FFN, and binary+bypass FFN with matched reporting for validation perplexity, storage, and training stability.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer validation of binary FFN FP32 bypass
- Success threshold: Binary+bypass improves final validation perplexity over binary-only by at least 3% relative across at least 3 seeds without instability, while preserving at least 50% effective FFN storage reduction versus dense.
- Stop condition: Stop if binary+bypass fails to beat binary-only on mean validation perplexity, shows repeated instability, or requires FP32 storage that erases the targeted storage reduction.

## Evidence references

- Artifact root: `<local-path>/projects/binary-weight-ffn-with-fp32-residual-bypass-fc5fa4d60331`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
