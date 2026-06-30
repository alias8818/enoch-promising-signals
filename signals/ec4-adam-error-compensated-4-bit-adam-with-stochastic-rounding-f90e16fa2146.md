# EC4-Adam: error-compensated 4-bit Adam with stochastic rounding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ec4-adam-error-compensated-4-bit-adam-with-stochastic-rounding-f90e16fa2146`
Run ID: `ec4-adam-error-compensated-4-bit-adam-with-stochastic-rounding-f90e16fa2146-20260612T000142851733+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b166d9d7a0eb

## What looked useful

Stochastic rounding alone rescued the toy MLP relative to deterministic 4-bit quantization, but adding fp32 residual error compensation worsened mean MLP loss/accuracy versus stochastic rounding alone and catastrophically destabilized the ill-conditioned quadratic through exploding second-moment quantization error.

## Boundaries and scale limits

No packed 4-bit kernel, throughput benchmark, memory-saving implementation, language-model training, distributed run, or large-corpus validation was performed. EC residuals were fp32 diagnostic tensors, so memory benefit was not validated.

## Claim scope

Bounded local tests of per-tensor signed symmetric 4-bit Adam moment quantization on a 256D ill-conditioned quadratic and a small spiral-classification MLP show that naive error-compensated stochastic 4-bit moment quantization is not a reliable improvement over stochastic rounding alone.

## Why it stopped

Proxy/local early falsification: direct small-task evidence found instability on an ill-conditioned convex objective and no improvement over the simpler stochastic-rounding 4-bit control on the neural toy task; this is not full-scale validation.

## Recommended next action

Stop this EC4-Adam variant as no-paper evidence; the next bounded test should replace naive per-tensor second-moment quantization with a blockwise nonnegative/log-domain quantizer and bounded residuals before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blockwise nonnegative EC4-Adam second-moment quantization
- Success threshold: On 5 seeds, blockwise nonnegative EC4-Adam must keep quadratic final loss within 10x of fp32 Adam's loss AUC or at least 100x below stochastic 4-bit, and must match or exceed stochastic 4-bit MLP accuracy while reducing second-moment quantization MSE.
- Stop condition: Stop if blockwise/nonnegative residual control still produces quadratic loss above deterministic 4-bit or MLP accuracy below stochastic 4-bit, because the EC mechanism is not earning added complexity.

## Evidence references

- Artifact root: `<local-path>/projects/ec4-adam-error-compensated-4-bit-adam-with-stochastic-rounding-f90e16fa2146`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
