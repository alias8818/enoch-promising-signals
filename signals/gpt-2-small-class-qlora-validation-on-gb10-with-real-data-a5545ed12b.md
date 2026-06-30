# GPT-2-small-class QLoRA validation on GB10 with real data

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gpt-2-small-class-qlora-validation-on-gb10-with-real-data-a5545ed12b`
Run ID: `gpt-2-small-class-qlora-validation-on-gb10-with-real-data-a5545ed12b-20260605T143755321491+0000`

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

- Parent run decision: 4-bit Quantized Training with LoRA on GB10: enoch://control-plane/projects/4-bit-quantized-training-with-lora-on-gb10-8cf1e30d1921/runs/4-bit-quantized-training-with-lora-on-gb10-8cf1e30d1921-20260605T105530274318+0000
- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/ffc50c4ab94f

## What looked useful

Tier 1 direct QLoRA smoke and controlled run succeeded on GB10. Validation loss fell from 3.9781 to 3.6413 and perplexity fell from 53.42 to 38.14 on WikiText-2 validation after 80 LoRA update steps; training throughput was 6,763.9 tokens/s overall with MemAvailable above 113.6 GiB.

## Boundaries and scale limits

Single seed, GPT-2 small only, 20,480 training tokens, 8,192 validation tokens, sequence length 128, 80 adapter steps, no dense fine-tune or standard LoRA baseline, no downstream task evaluation, no long-run stability or robustness checks.

## Claim scope

On GB10/aarch64 with torch 2.12.0+cu130 and bitsandbytes 0.49.2, GPT-2 small can be loaded in 4-bit NF4 with LoRA adapters and trained on real WikiText-2 text for a small controlled run, producing a measurable held-out validation loss/perplexity reduction.

## Why it stopped

Tier 1 direct validation reached the required small-test threshold and produced useful no-paper evidence; publication readiness would require replicated medium-scale controls and robustness evidence.

## Recommended next action

Run a bounded medium deepen test with three seeds, a larger WikiText/OpenWebText subset, sequence length at least 512, and a matched non-quantized LoRA control before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replicated medium GPT-2 QLoRA vs standard LoRA control on GB10
- Success threshold: QLoRA mean validation-loss reduction is within 0.05 loss of matched standard LoRA or better across three seeds, no seed regresses validation loss, and GB10 MemAvailable remains above 20 GiB throughout.
- Stop condition: Stop if QLoRA fails to run at sequence length 512 on GB10, if any replicated seed shows validation loss regression after the planned training budget, or if memory pressure drops MemAvailable below 20 GiB.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-qlora-validation-on-gb10-with-real-data-a5545ed12b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
