# INT2-plus-Residual GPT-2 CPU Inference via Sensitivity Sidebands

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int2-plus-residual-gpt-2-cpu-inference-via-sensitivity-sidebands-d34daac73933`
Run ID: `int2-plus-residual-gpt-2-cpu-inference-via-sensitivity-sidebands-d34daac73933-20260529T174003730177+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/396d993366fb

## What looked useful

Sensitivity ranking is a real mechanism signal: at 2% sideband budget it reduced relative output error by a median 7.63% versus 2.05% for random residuals. However, the main benchmark showed median relative MSE 0.402 and median speedup only 0.0245x versus FP32 at 2% sideband budget, making the tested CPU inference path negative.

## Boundaries and scale limits

No pretrained GPT-2 weights, perplexity, autoregressive decoding, INT8 baseline, or custom packed INT2/fused sideband kernel were evaluated. Results are bounded to NumPy CPU matmul proxies with synthetic Gaussian activations and weights matching GPT-2-small layer dimensions.

## Claim scope

On synthetic GPT-2-small-shaped CPU linear matmuls, sensitivity-selected residual sidebands recover more output error than random sidebands, but the naive INT2-plus-sideband path is not viable for CPU inference because sideband application dominates latency and reconstruction remains poor at practical sideband budgets.

## Why it stopped

The bounded proxy test found a useful sideband-selection signal but falsified the naive CPU inference path: sidebands were slower than FP32 and did not recover enough fidelity. This is not a full GPT-2 validation.

## Recommended next action

Stop this run as a bounded proxy/early falsification; only revisit if implementing a fused packed INT2 CPU kernel and evaluating pretrained GPT-2-small perplexity/tokens-per-second against FP32 and INT8 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused packed INT2 sideband kernel on pretrained GPT-2-small
- Success threshold: At least 1.3x tokens-per-second versus an optimized FP32 CPU baseline, no more than 10% slowdown versus INT8, and less than 5% relative perplexity degradation at a sideband storage ratio below 0.20x FP32.
- Stop condition: Stop if the fused kernel remains slower than FP32 at 2-4% sideband budget, or if pretrained GPT-2-small perplexity degrades by more than 10% at all sideband budgets below 0.20x FP32 storage.

## Evidence references

- Artifact root: `<local-path>/projects/int2-plus-residual-gpt-2-cpu-inference-via-sensitivity-sidebands-d34daac73933`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
