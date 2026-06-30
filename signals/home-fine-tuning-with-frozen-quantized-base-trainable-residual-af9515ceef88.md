# Home Fine-Tuning with Frozen Quantized Base + Trainable Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-fine-tuning-with-frozen-quantized-base-trainable-residual-af9515ceef88`
Run ID: `home-fine-tuning-with-frozen-quantized-base-trainable-residual-af9515ceef88-20260523T185815477474+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/00855c71463b

## What looked useful

Dense residual adaptation improved validation accuracy from 0.1727 for the frozen quantized base to 0.4937, compared with 0.5433 for full fine-tuning. LoRA rank 8 reduced CE but fell to 0.0912 argmax accuracy, so the low-rank parameter-efficient version was not supported by this proxy.

## Boundaries and scale limits

The experiment used an MLP proxy, synthetic token inputs, deterministic teacher labels, 3 seeds, and sub-minute training runs. It did not test GPT-2-small-class language modeling, natural text, instruction tuning, long runs, optimizer memory pressure, save/load persistence, or matched trainable-parameter efficiency.

## Claim scope

In a small synthetic teacher/student token-classification proxy, a frozen 4-bit quantized base with dense trainable additive residual matrices can adapt to a shifted target distribution and recover most of the accuracy gap to full fine-tuning.

## Why it stopped

No-paper useful signal: the mechanism worked in a toy proxy, but this is not direct/full validation of home language-model fine-tuning and dense residuals were not parameter-efficient enough to support a practical claim.

## Recommended next action

Run a bounded GPT-2-small-class text experiment comparing frozen 4-bit base plus residual adapters against LoRA/QLoRA and full fine-tuning under matched trainable-parameter and memory budgets; stop paper pursuit unless the residual variant beats LoRA at similar memory or reaches full-finetune quality with materially lower writable state.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small residual adapters over a frozen 4-bit base
- Success threshold: Residual adapter validation perplexity is at least 3% better than LoRA/QLoRA at comparable trainable parameter count and no more than 10% worse than full fine-tuning while using materially less writable state.
- Stop condition: Stop if residual adapters cannot beat the frozen base by at least 20% validation-loss reduction after the same token budget, or if they require dense residual state close to full fine-tuning to match LoRA.

## Evidence references

- Artifact root: `<local-path>/projects/home-fine-tuning-with-frozen-quantized-base-trainable-residual-af9515ceef88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
