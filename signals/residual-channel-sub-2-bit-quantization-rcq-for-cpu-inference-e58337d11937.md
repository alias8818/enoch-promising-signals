# Residual-Channel Sub-2-bit Quantization (RCQ) for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-sub-2-bit-quantization-rcq-for-cpu-inference-e58337d11937`
Run ID: `residual-channel-sub-2-bit-quantization-rcq-for-cpu-inference-e58337d11937-20260611T074423773267+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5a7e9b2e7706

## What looked useful

RCQ energy selection is a real error-reduction mechanism versus binary and random residual selection, but the tested formulation is accuracy-dominated by a straightforward same-budget selected 2-bit baseline across all three scenarios and three seeds.

## Boundaries and scale limits

No pretrained transformer weights, perplexity, downstream accuracy, or bit-packed CPU inference kernels were tested; dense NumPy matmul timings are not throughput evidence for quantized inference.

## Claim scope

For a NumPy-only synthetic/proxy layer test of per-output-channel binary weights plus selected residual binary channels at 1.25, 1.50, and 1.75 average weight bits, residual-energy channel selection improves output error over random residual selection but does not beat selected 2-bit channels at the same average bit budget.

## Why it stopped

Proxy/local evidence is mixed and insufficient for a paper: RCQ helps versus random selection but loses to the stronger same-budget 2-bit control, and no real-model or quantized-kernel evidence was produced.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement a bit-packed CPU kernel and evaluate whether RCQ's binary add/sub structure offsets its accuracy gap against selected 2-bit rows.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bit-packed CPU RCQ versus selected 2-bit row kernels
- Success threshold: RCQ must either match selected 2-bit output relative MSE within 5% at the same average bit budget or deliver at least 20% lower CPU latency at matched output-error levels on real or model-derived weights.
- Stop condition: Stop if RCQ remains accuracy-dominated by selected 2-bit rows and shows less than 20% CPU latency advantage in the quantized kernel benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-sub-2-bit-quantization-rcq-for-cpu-inference-e58337d11937`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
