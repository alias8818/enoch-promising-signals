# GPTQ vs RTN on GPT-2-small: perplexity and throughput frontier

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gptq-vs-rtn-on-gpt-2-small-perplexity-and-throughput-frontier-4f769a40b4ee`
Run ID: `gptq-vs-rtn-on-gpt-2-small-perplexity-and-throughput-frontier-4f769a40b4ee-20260621T064252576688+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/72aaddea9ab3

## What looked useful

Calibrated run: dense FP16 perplexity 64.4056; RTN 4-bit fake quant perplexity 74.8906 (+10.4850); GPTQ-style 4-bit fake quant perplexity 69.0613 (+4.6557). The quality mechanism is supported locally, but packed-kernel throughput remains unvalidated.

## Boundaries and scale limits

Evaluation used 32 calibration blocks and 64 evaluation blocks at sequence length 128, with embeddings and layer norms left dense. Throughput was measured on unpacked/dequantized FP16 weights, not true packed int4 kernels, so serving frontier claims are not closed.

## Claim scope

On GPT-2-small over a bounded WikiText-2 sample, 4-bit group-size-128 Hessian-corrected fake quantization of all Conv1D projection weights preserved perplexity better than RTN fake quantization under the same harness.

## Why it stopped

The run produced direct bounded perplexity evidence but only fake-quant throughput, so it cannot validate the full perplexity-throughput frontier claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should run actual packed int4 GPTQ and RTN kernels on the same GPT-2-small WikiText-2 harness and report prefill/decode throughput separately.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed int4 GPTQ vs RTN throughput on GPT-2-small
- Success threshold: GPTQ perplexity delta versus dense is at least 25% lower than RTN's delta, and packed GPTQ decode throughput is within 10% of packed RTN on the same prompt/batch settings.
- Stop condition: Stop if no bounded packed RTN and GPTQ kernel path can be made to run locally, or if GPTQ loses its perplexity advantage on the fixed split.

## Evidence references

- Artifact root: `<local-path>/projects/gptq-vs-rtn-on-gpt-2-small-perplexity-and-throughput-frontier-4f769a40b4ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
