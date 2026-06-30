# Activation-Aware Grouping for 4-bit KV Cache on Consumer GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-aware-grouping-for-4-bit-kv-cache-on-consumer-gpus-37b0ad87f180`
Run ID: `activation-aware-grouping-for-4-bit-kv-cache-on-consumer-gpus-37b0ad87f180-20260608T130021812614+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0fbedae6cd8d

## What looked useful

Activation-aware sorting is a plausible error-reduction mechanism relative to contiguous channel groups, with medium group-size-16 mean output relative MSE 0.06740 versus contiguous 0.10372. However random grouping reached 0.07706 at group size 16 and beat activation-sorted at group size 32, so the specific activation-aware rule is not robustly supported.

## Boundaries and scale limits

No real LLM KV traces, no packed int4 KV cache kernel, no perplexity/task evaluation, no long-context serving throughput, and only small/medium synthetic tensor shapes up to batch=1, heads=8, seq_len=512, dim=128.

## Claim scope

Synthetic GB10 PyTorch probe of 4-bit grouped K/V quantization with heteroskedastic channel activations; activation-RMS sorting reduced attention-output error versus contiguous grouping but was not consistently better than random grouping.

## Why it stopped

Proxy synthetic evidence is mixed: it supports improvement over contiguous grouping but early-falsifies a broad claim that activation-aware grouping reliably dominates simple non-contiguous grouping.

## Recommended next action

Stop this run as no-paper useful signal; next, run the same grouping rules on saved real K/V traces from a small transformer and compare perplexity or next-token loss plus packed-kernel decode throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Trace Validation for Activation-Aware 4-bit Grouping
- Success threshold: Activation-sorted grouping must reduce mean attention-output relative MSE or loss delta by at least 15% versus both contiguous and the best random baseline at the same group size, with no measurable decode throughput regression beyond 5%.
- Stop condition: Stop if activation-sorted fails to beat the best random grouping by at least 5% on real traces for both group sizes, or if packed-kernel throughput regresses by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-grouping-for-4-bit-kv-cache-on-consumer-gpus-37b0ad87f180`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
