# 1.58-bit Activations + Statistical Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-58-bit-activations-statistical-residual-f0022421aadb`
Run ID: `1-58-bit-activations-statistical-residual-f0022421aadb-20260629T114722038712+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8d925090100d

## What looked useful

Across five seeds and three activation scenarios, per-code residuals reduced matched relative logit RMSE by 1.89% on average versus per-channel ternary quantization. The effect was scenario-dependent: ReLU mean reduction 3.04%, shifted activation mean reduction 2.65%, Gaussian/tanh-like mean change -0.005%. Mean matched top-1 agreement gain was 0.78 percentage points overall.

## Boundaries and scale limits

Synthetic MLP activations only; no transformer, LLM, real dataset, quantized kernel, throughput, or residual-metadata overhead validation.

## Claim scope

In deterministic NumPy synthetic teacher-network probes, calibration-set per-code residuals for ternary 1.58-bit-style activations reduce downstream logit RMSE for skewed ReLU and shifted activation distributions, but provide no useful improvement for symmetric Gaussian/tanh-like activations.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and mixed by activation distribution.

## Recommended next action

Run a bounded direct follow-up on real transformer hidden states, measuring activation-site reconstruction and perplexity impact before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Test per-code statistical residuals on real transformer activation sites
- Success threshold: At skewed activation sites, per-code residuals reduce relative reconstruction error by at least 2% and improve or preserve perplexity versus per-channel ternary without worsening symmetric control sites by more than 0.5%.
- Stop condition: Stop if real transformer activations show less than 1% reconstruction improvement at skewed sites or if perplexity worsens despite reconstruction gains.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-activations-statistical-residual-f0022421aadb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
