# 2-Bit KV Cache Importance Eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-importance-eviction-c46025d30d04`
Run ID: `2-bit-kv-cache-importance-eviction-c46025d30d04-20260524T215203121361+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e971ea2dbc86

## What looked useful

Standalone importance eviction was not competitive with 2-bit quantize-all: MSE was 1.47x, 2.86x, and 2.35x worse across diffuse_iid, moderate_local, and spiky_recurrent scenarios. Importance retention beat random in two of three scenarios but lost to recency in local and spiky settings. An extra-budget hybrid of 2-bit quantize-all plus exact important tokens reduced MSE versus quantize-all by 15.7% to 23.3%, suggesting importance may be useful for mixed precision rather than full eviction.

## Boundaries and scale limits

No pretrained model, no perplexity/task benchmark, no packed 2-bit kernel, no GPU decode throughput measurement, and no real long-context workload. The hybrid diagnostic used extra budget and is not an equal-budget quality claim.

## Claim scope

Dependency-free synthetic causal attention reconstruction at seq_len=192, dim=32, 12 trials per scenario. Standalone online importance eviction with fp32 retention of seq_len/16 tokens was compared against 2-bit quantize-all, recency retention, and random retention controls under an approximate equal scalar-bit budget.

## Why it stopped

Bounded synthetic evidence is a useful proxy signal but early-falsifies standalone importance eviction as a replacement for 2-bit quantize-all under the tested equal-budget reconstruction metric; it is not full validation on real models.

## Recommended next action

Do not write a paper from this run; run a bounded follow-up that tests equal-budget mixed-precision 2-bit KV caching on a small pretrained transformer with perplexity and retrieval metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equal-Budget Mixed-Precision 2-Bit KV Importance Probe
- Success threshold: At the same total KV bit budget, importance mixed precision reduces perplexity or retrieval error versus uniform 2-bit and recency controls by at least 5% relative without increasing measured cache bytes.
- Stop condition: Stop if equal-budget importance mixed precision fails to beat either uniform 2-bit quantization or recency mixed precision on both perplexity and retrieval metrics in a small pretrained-transformer test.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-importance-eviction-c46025d30d04`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
