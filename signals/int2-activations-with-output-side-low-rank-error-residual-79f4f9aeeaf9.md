# INT2 Activations with Output-Side Low-Rank Error Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-activations-with-output-side-low-rank-error-residual-79f4f9aeeaf9`
Run ID: `int2-activations-with-output-side-low-rank-error-residual-79f4f9aeeaf9-20260630T133933687682+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5ae17bc3184a

## What looked useful

Oracle low-rank error structure is not sufficient for a deployable output-side residual. At rank 128 with structured weights, the oracle recovered about 97.4% of correlated layernorm-like error while the learned output-only residual worsened error by 13.5%. Heavy-tail structured activations were the positive bounded case, with learned rank-128 recovery around 80.2%.

## Boundaries and scale limits

No pretrained transformer activations, end-to-end perplexity, task accuracy, fused INT2 kernels, or latency/throughput production path were tested. Evidence is limited to GPU tensor experiments with synthetic activation distributions and 8192 calibration/test rows.

## Claim scope

On synthetic 768x768 linear projections with rowwise symmetric INT2 activation quantization, held-out output quantization error can be low-rank, but a deployable output-only low-rank residual Y_q C_r is not generally reliable. It improves heavy-tail and some structured-weight cases, but worsens correlated layernorm-like activations despite strong oracle low-rank recoverability.

## Why it stopped

Proxy/medium local evidence is mixed and early-falsifies the general output-only mechanism: the deployable residual can fail even when the held-out output error has a strong low-rank oracle correction.

## Recommended next action

Stop this broad output-only residual claim; run a bounded follow-up that conditions the residual on quantization scales or activation-side error features and evaluates real GPT-2-small layer activations before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Condition INT2 activation residuals on quantization side information
- Success threshold: At rank 64 or 128, recover at least 50% of INT2 output error on correlated layernorm-like synthetic data and at least 30% on real GPT-2-small held-out layer activations without worsening any tested layer relative to plain INT2.
- Stop condition: Stop if side-information-conditioned residuals still recover less than 15% of error or worsen any correlated/real activation control at rank 128.

## Evidence references

- Artifact root: `<local-path>/projects/int2-activations-with-output-side-low-rank-error-residual-79f4f9aeeaf9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
