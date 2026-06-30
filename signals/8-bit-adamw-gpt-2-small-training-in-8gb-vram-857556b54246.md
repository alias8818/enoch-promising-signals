# 8-bit AdamW GPT-2-Small Training in 8GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-gpt-2-small-training-in-8gb-vram-857556b54246`
Run ID: `8-bit-adamw-gpt-2-small-training-in-8gb-vram-857556b54246-20260528T235613219050+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e74519f2f76a

## What looked useful

8-bit AdamW reduced GPT-2-small optimizer state from about 0.927 GiB to 0.236 GiB and reduced end-to-end peak CUDA memory by about 0.69 GiB. This was enough to keep batch-4 full-context training below 8 GiB reserved memory where standard AdamW crossed it, but standard AdamW also fits batch 1 comfortably.

## Boundaries and scale limits

Synthetic-token, 2-3 step probes only; no real dataset convergence, no long training, no enforced hard 8 GB device limit, and GB10 does not report conventional discrete VRAM capacity through nvidia-smi.

## Claim scope

On this GB10 CUDA/PyTorch stack, synthetic GPT-2-small training steps with sequence length 1024, batch size 4, bf16 autocast, and bitsandbytes AdamW8bit completed with 6.802 GiB peak CUDA allocated and 7.438 GiB peak CUDA reserved; standard AdamW completed but crossed 8 GiB reserved at 8.143 GiB. Batch size 5 exceeded the 8 GiB target for both optimizers.

## Why it stopped

The result is a bounded synthetic memory/execution signal, not a full validation; it does not show 8-bit AdamW is uniquely necessary for GPT-2-small in 8 GiB.

## Recommended next action

Stop this run as a no-paper useful signal; deepen only with an enforced 8 GiB GPU-memory limit and real-token GPT-2-small training long enough to compare convergence and stability.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-capped 8 GiB GPT-2-small AdamW8bit training boundary
- Success threshold: AdamW8bit completes a real-token GPT-2-small run under an enforced 8 GiB limit at a configuration where standard AdamW reliably OOMs or must use a materially smaller effective token budget, with no short-run loss instability.
- Stop condition: Stop if AdamW also fits the same practical configuration under the hard 8 GiB limit, if AdamW8bit cannot complete the target run, or if loss diverges relative to AdamW in the short-run comparison.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-gpt-2-small-training-in-8gb-vram-857556b54246`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
