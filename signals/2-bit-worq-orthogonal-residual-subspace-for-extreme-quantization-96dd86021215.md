# 2-bit WORQ: Orthogonal Residual Subspace for Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-worq-orthogonal-residual-subspace-for-extreme-quantization-96dd86021215`
Run ID: `2-bit-worq-orthogonal-residual-subspace-for-extreme-quantization-96dd86021215-20260621T194502219315+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/934896233762

## What looked useful

Orthogonal residuals improved output MSE over a bare 2-bit base but consistently underperformed the same-rank unconstrained low-rank residual control. Across 144 main conditions, global orthogonal residual improved 7.35% vs 2-bit base compared with 18.46% for unconstrained residual, had 1.161x the output MSE of the unconstrained residual on average, and beat it in 0/144 conditions. Per-row orthogonal residual was similar or worse.

## Boundaries and scale limits

No full LLM weights, perplexity, downstream accuracy, packed-kernel latency, or memory-footprint validation. Results are matrix and single-layer output reconstruction proxies only.

## Claim scope

Bounded proxy test of 2-bit per-row quantized square matrices with same-rank low-rank residual adapters on synthetic Gaussian, low-rank-plus-noise, heavy-tailed, and block-correlated matrix families at dimensions 256, 512, and 1024.

## Why it stopped

Proxy/early falsification: the proposed orthogonal residual mechanism did not beat the simpler same-rank unconstrained residual control under matrix and layer-output reconstruction tests.

## Recommended next action

Stop paper pursuit from this proxy result; only continue with a bounded GPT-2-small layer/perplexity follow-up if direct model evidence is required to overturn the early falsification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small direct check for 2-bit orthogonal residual quantization
- Success threshold: Orthogonal residual must improve validation perplexity or layer-output MSE by at least 5% over the same-rank unconstrained residual at identical storage budget, while preserving the 2-bit base.
- Stop condition: Stop if orthogonal residual is not better than the unconstrained residual on both layer-output MSE and validation perplexity for the tested GPT-2-small layers.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-worq-orthogonal-residual-subspace-for-extreme-quantization-96dd86021215`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
