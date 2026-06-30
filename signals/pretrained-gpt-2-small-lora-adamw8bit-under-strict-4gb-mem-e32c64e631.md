# Pretrained GPT-2-small LoRA+AdamW8bit under strict 4GB memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pretrained-gpt-2-small-lora-adamw8bit-under-strict-4gb-mem-e32c64e631`
Run ID: `pretrained-gpt-2-small-lora-adamw8bit-under-strict-4gb-mem-e32c64e631-20260621T053933365747+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: LoRA + 8-bit AdamW for Sub-4GB VRAM Fine-tuning: enoch://control-plane/projects/lora-8-bit-adamw-for-sub-4gb-vram-fine-tuning-b100bd0e32f0/runs/lora-8-bit-adamw-for-sub-4gb-vram-fine-tuning-b100bd0e32f0-20260621T052142131213+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/41fa2e2055c3

## What looked useful

The direct target path is feasible: pretrained GPT-2-small plus PEFT LoRA plus AdamW8bit completed forward, backward, and optimizer steps under 4 GB. The control indicates the main useful result is practical feasibility, not a paper-ready optimizer-memory advantage.

## Boundaries and scale limits

Tiny local text corpus, 32 optimizer steps, batch size 1, sequence length 128, no validation metric, no convergence claim, no frontier search, no larger model, no long-context or multi-seed robustness. Standard AdamW also fit under 4 GB in the same LoRA setup, so AdamW8bit was not shown to be decisive at this scale.

## Claim scope

On this GB10 host with swap disabled, pretrained openai-community/gpt2 can run a real LoRA causal-LM training loop with bitsandbytes AdamW8bit for 32 steps at batch size 1 and sequence length 128 under a 4096 MiB RSS guard; BF16 peak RSS was 1832.68 MiB and FP32 AdamW8bit also stayed below the guard.

## Why it stopped

Tier 1 direct small test supports feasibility but lacks convergence, robustness, and an optimizer-memory advantage; it is not paper-positive.

## Recommended next action

Stop as no-paper useful signal; next bounded action is to sweep batch size and sequence length under the same 4 GB guard for AdamW8bit versus standard AdamW to identify whether 8-bit optimizer state materially extends the GPT-2-small LoRA feasibility frontier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Map GPT-2-small LoRA 4GB feasibility frontier for AdamW8bit versus AdamW
- Success threshold: Find at least one configuration where AdamW8bit completes 16 or more real training steps under 4096 MiB RSS while standard AdamW fails the guard or has at least 10% higher peak memory, with comparable loss sanity checks.
- Stop condition: Stop if both optimizers fit or fail together across the sweep frontier, or if failures are caused by unrelated runtime/library issues rather than memory pressure.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-gpt-2-small-lora-adamw8bit-under-strict-4gb-mem-e32c64e631`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
