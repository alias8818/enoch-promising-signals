# 4-bit Gradients with Residual Error Compensation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-gradients-with-residual-error-compensation-74ff73c2871b`
Run ID: `4-bit-gradients-with-residual-error-compensation-74ff73c2871b-20260523T110534573378+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

Residual error feedback reduced cumulative gradient-sum relative error from 0.6306 to 0.00863 in a 20-seed diagnostic, but the 20-seed training comparison showed only a tiny residual-over-plain 4-bit accuracy delta of +0.0016 with a 95% CI crossing zero.

## Boundaries and scale limits

Evidence is limited to a small synthetic classification task plus a synthetic gradient-stream diagnostic. It does not validate large language model training, distributed gradient communication, packed 4-bit throughput, adaptive optimizers, or full-scale convergence.

## Claim scope

On a toy PyTorch MLP spiral-classification task, 4-bit gradients train successfully and residual error compensation is directionally but not statistically convincingly better than plain 4-bit gradients; on synthetic gradient streams, residual feedback strongly reduces cumulative quantization drift.

## Why it stopped

No-paper useful signal: local evidence supports the cumulative-error mechanism but the toy training advantage of residual 4-bit over plain 4-bit is small and statistically unresolved.

## Recommended next action

Run a bounded deepen follow-up on a tiny transformer language-modeling task with real validation perplexity before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual 4-bit gradients on a tiny transformer language-modeling proxy
- Success threshold: Residual 4-bit must improve paired validation loss or perplexity versus plain 4-bit by a practically meaningful margin with confidence intervals excluding zero, while staying within a small gap to fp32.
- Stop condition: Stop if residual 4-bit does not beat plain 4-bit on paired validation loss/perplexity, or if implementation overhead dominates without a convergence benefit.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-gradients-with-residual-error-compensation-74ff73c2871b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
