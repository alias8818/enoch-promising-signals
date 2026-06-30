# CPU Data-Parallel + PowerSGD: Tiny Transformer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-data-parallel-powersgd-tiny-transformer-3f9a798a8caa`
Run ID: `cpu-data-parallel-powersgd-tiny-transformer-3f9a798a8caa-20260621T084443244490+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92728ff62b1b

## What looked useful

PowerSGD is mechanically viable for tiny-transformer-shaped gradients and preserves toy 20-step eval loss within about 0.00008 of dense averaging, but local CPU compression overhead dominates dense averaging and low ranks show 0.63-0.95 relative gradient error.

## Boundaries and scale limits

No real multi-process, multi-node, network, PyTorch DDP, or GPT-2-small-class training was measured. Data are synthetic random tokens and the confirmation is 20 toy steps.

## Claim scope

A single-process NumPy CPU proxy with a 12,800-parameter one-block causal attention + MLP language model shows that PowerSGD rank 1/2/4/8 reducers cut simulated gradient bytes by 18.60x/9.30x/4.65x/2.33x versus dense averaging, but are slower than dense in local reducer time and have high relative gradient reconstruction error.

## Why it stopped

Proxy/local CPU evidence is useful but not sufficient for a paper or a runtime-advantage claim; dense averaging was faster in this bounded setup.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run a bounded real multi-process CPU distributed benchmark with measured communication time to test whether byte savings overcome compression overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Multi-Process PowerSGD Tiny Transformer Benchmark
- Success threshold: PowerSGD rank 4 or 8 improves median end-to-end step time by at least 10% versus dense while final validation loss is within 1% of dense on the same bounded workload.
- Stop condition: Stop if dense communication is under 10% of step time, if PowerSGD is not at least 5% faster after calibration, or if validation loss delta exceeds 1%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-data-parallel-powersgd-tiny-transformer-3f9a798a8caa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
