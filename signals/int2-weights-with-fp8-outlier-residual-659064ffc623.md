# INT2 weights with FP8 outlier residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-weights-with-fp8-outlier-residual-659064ffc623`
Run ID: `int2-weights-with-fp8-outlier-residual-659064ffc623-20260628T210157759422+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ba6eef76f325

## What looked useful

At 4% residual density and 2.68 effective bits/weight, output relative RMSE improved 1.082x on Gaussian weights, 1.241x on student-t df=3 weights, and 1.276x on 1% mixture-outlier weights versus INT2-only. Absolute output relative RMSE remained high at 0.41519, 0.53472, and 0.58375 respectively.

## Boundaries and scale limits

No transformer perplexity, downstream accuracy, packed sparse kernel, exact hardware FP8 encoding, large model, or real serving throughput was tested. Results are limited to NumPy CPU synthetic matrices and random Gaussian activations.

## Claim scope

Synthetic 512x512 linear-layer proxy: per-group affine INT2 weights plus sparse FP8 E4M3-proxy residuals selected by largest quantization error reduce reconstruction and output error, with the largest gains on heavy-tailed/outlier weight distributions.

## Why it stopped

Closed as no-paper useful signal because the local proxy supports the outlier-residual mechanism but does not validate model quality or hardware efficiency.

## Recommended next action

Run a bounded deepen test on real GPT-2-small-class transformer weights with an INT4/dense control, measuring perplexity or next-token loss plus packed storage and kernel/runtime overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: INT2 plus sparse FP8 residual on GPT-2-small-class weights
- Success threshold: At <=3.0 effective bits/weight, INT2 plus FP8 residual should cut at least 50% of the INT2-only perplexity or loss degradation toward the INT4 control without more than 20% runtime overhead versus the chosen low-bit baseline.
- Stop condition: Stop if real-model loss remains closer to INT2-only than INT4 at 3.0 effective bits/weight, or if sparse residual runtime overhead exceeds 20% before quality approaches INT4.

## Evidence references

- Artifact root: `<local-path>/projects/int2-weights-with-fp8-outlier-residual-659064ffc623`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
