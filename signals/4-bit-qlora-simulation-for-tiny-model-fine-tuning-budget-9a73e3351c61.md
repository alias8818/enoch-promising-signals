# 4-bit QLoRA simulation for tiny model fine-tuning budget

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-qlora-simulation-for-tiny-model-fine-tuning-budget-9a73e3351c61`
Run ID: `4-bit-qlora-simulation-for-tiny-model-fine-tuning-budget-9a73e3351c61-20260605T004515788468+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/053a5e17c8ff

## What looked useful

4-bit quantization error was small in the proxy and q4 LoRA tracked FP LoRA: at 1024 examples q4 LoRA reached mean val NLL 3.1716 and 0.606 adaptation recovery versus FP LoRA 3.1864 and 0.591, while full fine-tuning reached 3.5183 and 0.273. At 64 examples both LoRA variants were worse than the unadapted base, so the mechanism is budget-sensitive.

## Boundaries and scale limits

Synthetic Markov table only; no transformer layers, real corpus, NF4/double quantization, optimizer-state behavior, activation memory pressure, GPU kernels, or GPT-2-small-class baseline were tested.

## Claim scope

In a controlled 64-token Markov next-token adaptation simulation with a rank-4 target shift, per-row simulated 4-bit dequantized bases did not materially degrade rank-4 LoRA adaptation relative to FP-base LoRA at the 1024-example budget; both LoRA variants failed or were neutral at smaller 64 and 256 example budgets.

## Why it stopped

Synthetic proxy evidence is useful for mechanism screening but is not sufficient for a paper or for claims about real 4-bit QLoRA fine-tuning.

## Recommended next action

Stop this run as a proxy useful signal; the concrete next action is a bounded tiny-transformer QLoRA follow-up on a real text adaptation task with validation perplexity and memory telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer 4-bit QLoRA adaptation under small data budgets
- Success threshold: 4-bit QLoRA recovers at least 90% of FP LoRA improvement over the unadapted base at one or more practical small-data budgets without more than 10% worse validation NLL, and shows at least 4x frozen-base weight-memory reduction.
- Stop condition: Stop as negative if 4-bit QLoRA is more than 10% worse than FP LoRA validation NLL at all tested budgets or if it fails to improve over the unadapted base outside the extreme-low-data budget.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-qlora-simulation-for-tiny-model-fine-tuning-budget-9a73e3351c61`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
