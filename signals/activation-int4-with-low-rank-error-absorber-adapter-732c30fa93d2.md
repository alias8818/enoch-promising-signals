# Activation INT4 with low-rank error-absorber adapter

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-int4-with-low-rank-error-absorber-adapter-732c30fa93d2`
Run ID: `activation-int4-with-low-rank-error-absorber-adapter-732c30fa93d2-20260620T002102198799+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b77064485f94

## What looked useful

Across seeds 732-734, rank-64 improved structured-lowdim held-out MSE by 20.08-24.53% and rank-16/64 improved outlier-channel MSE by 8.34-11.12%, while shuffled-error controls were negative. Gaussian activations were consistently negative, from -0.24% to -2.55% depending on rank.

## Boundaries and scale limits

No transformer, language-model loss, real text calibration set, production INT4 kernel, layernorm/residual stack, or end-to-end fine-tuning was tested. Dimensions were 512 x 512 with 8192 calibration and 4096 held-out synthetic samples across three seeds.

## Claim scope

Synthetic single-linear-layer probe: an inference-time low-rank weight-delta adapter fed by INT4-dequantized activations reduced held-out activation-quantization output MSE for structured low-dimensional and outlier-channel activation distributions, but not for isotropic Gaussian activations.

## Why it stopped

This run produced a proxy/local mechanism signal, not direct LLM evidence; the current evidence is useful but insufficient for a paper or practical quantization claim.

## Recommended next action

Run one bounded real-model follow-up on a GPT-2-small-class or smaller transformer with real text calibration, per-layer activation INT4, and matched LoRA/control adapters before considering any scale-out claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer validation of INT4 activation low-rank error absorbers
- Success threshold: At least 20% reduction in INT4-induced held-out loss/perplexity degradation versus no-adapter baseline, and clear improvement over matched shuffled or ordinary low-rank controls in at least two independent seeds.
- Stop condition: Stop if real-model held-out loss improvement is below 5% of the INT4-induced degradation or does not beat matched controls across two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/activation-int4-with-low-rank-error-absorber-adapter-732c30fa93d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
