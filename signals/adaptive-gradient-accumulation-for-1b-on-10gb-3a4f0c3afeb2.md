# Adaptive gradient accumulation for 1B on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-gradient-accumulation-for-1b-on-10gb-3a4f0c3afeb2`
Run ID: `adaptive-gradient-accumulation-for-1b-on-10gb-3a4f0c3afeb2-20260602T213950851582+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4174e93ed6b9

## What looked useful

Persistent 1B bf16 AdamW memory was not the blocker under this PyTorch stack, but activation headroom was narrow: 2.5 GiB live scratch succeeded and 3.0 GiB failed under the 10 GiB cap. A measured-headroom scheduler proxy showed adaptive token-budget accumulation avoided fixed-microbatch OOMs on a variable-length trace.

## Boundaries and scale limits

No real 1B transformer architecture, sequence attention, data loader, throughput calibration, loss convergence, checkpointing, or long training run was executed. Activation behavior was measured with live scratch buffers and scheduler behavior was proxied with a synthetic variable-length trace.

## Claim scope

On GB10 with PyTorch 2.12 under an enforced 10 GiB CUDA allocator cap, 1B bf16 trainable parameters with AdamW can fit persistent parameter, dense-gradient, and optimizer-state memory at about 7.59 GiB peak allocated/reserved, leaving about 2.5 GiB of live activation/scratch headroom during backward. Adaptive gradient accumulation can help only when it keeps each individual microbatch below that headroom.

## Why it stopped

This is a bounded memory and scheduler-proxy result, not a direct 1B transformer training validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should train a real 1B-class transformer for a short fixed sequence-item budget under a hard 10 GiB cap, comparing fixed and adaptive accumulation on OOM rate, tokens/sec, and loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct 1B transformer adaptive accumulation under 10 GiB
- Success threshold: Adaptive accumulation completes the fixed sequence-item budget with zero OOMs, fixed accumulation has at least one OOM or requires lower throughput settings, and adaptive loss is no worse than fixed by 2% at matched tokens with tokens/sec no more than 10% lower.
- Stop condition: Stop if the real 1B transformer cannot materialize parameters plus optimizer state below 10 GiB, if every fixed microbatch that gives useful throughput exceeds activation headroom, or if adaptive overhead exceeds 10% without reducing OOMs.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-gradient-accumulation-for-1b-on-10gb-3a4f0c3afeb2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
