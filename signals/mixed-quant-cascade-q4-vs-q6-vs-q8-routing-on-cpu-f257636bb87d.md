# Mixed-quant cascade: Q4 vs Q6 vs Q8 routing on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `mixed-quant-cascade-q4-vs-q6-vs-q8-routing-on-cpu-f257636bb87d`
Run ID: `mixed-quant-cascade-q4-vs-q6-vs-q8-routing-on-cpu-f257636bb87d-20260620T223342339027+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/08f267be815c

## What looked useful

The low-bit stages were not confident enough often enough: full-run mean routing accepted 3.26% at Q4, 19.40% at Q6, and sent 77.34% to Q8. Mean additive cost was 15.9914 bit-MAC units versus 8.0 for Q8, and naive measured CPU latency was 8.786x Q8.

## Boundaries and scale limits

Synthetic linear task only; NumPy uses dequantized float32 matmuls rather than optimized int4/int6/int8 CPU kernels; no transformer/LLM serving workload, batching study, or production kernel dispatch was tested.

## Claim scope

In a seeded synthetic multiclass linear CPU probe with symmetric per-output-channel Q4/Q6/Q8 weight quantization, a confidence-gated additive Q4 -> Q6 -> Q8 cascade can match Q8 accuracy within about 0.2 percentage points but does not reduce expected compute cost.

## Why it stopped

Proxy/full-bounded synthetic evidence falsified the cost-saving success threshold: Q8-like accuracy required too much escalation, making average cascade cost about 2.0x always-Q8 rather than lower than Q8.

## Recommended next action

Stop this additive CPU cascade line as an early proxy falsification; only revisit if a follow-on design removes additive escalation cost or demonstrates a much higher low-bit acceptance rate on a direct target workload.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/mixed-quant-cascade-q4-vs-q6-vs-q8-routing-on-cpu-f257636bb87d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
