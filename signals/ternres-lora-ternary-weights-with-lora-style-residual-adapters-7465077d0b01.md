# TernRes-LoRA: Ternary Weights with LoRA-Style Residual Adapters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ternres-lora-ternary-weights-with-lora-style-residual-adapters-7465077d0b01`
Run ID: `ternres-lora-ternary-weights-with-lora-style-residual-adapters-7465077d0b01-20260628T073112432279+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c84415f6acd

## What looked useful

Dense mean test accuracy was 0.4814; post-training ternary mean was 0.3753; best TernRes-LoRA mean was 0.4655. LoRA residuals recovered 0.0902 absolute accuracy on average from a 0.1061 ternary drop, leaving a 0.0160 mean gap to dense.

## Boundaries and scale limits

CPU-only NumPy proxy; synthetic MLP teacher data; no transformer or real language-model task; no quantized inference kernel; no memory, latency, or energy validation; no parameter-matched dense residual control.

## Claim scope

On a deterministic synthetic two-layer classifier, frozen post-training ternary weights plus trained LoRA-style low-rank residual adapters recovered most of the accuracy lost by ternarization across three seeds.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy mechanism evidence, not direct language-model or hardware-efficiency validation.

## Recommended next action

Run a bounded tiny-transformer or GPT-2-small-class language-model follow-up with dense, ternary-only, LoRA-only, and TernRes-LoRA controls before considering scale-up or paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: TernRes-LoRA tiny language-model confirmation
- Success threshold: TernRes-LoRA should recover at least 50% of the ternary perplexity/loss degradation versus dense and outperform a parameter-matched LoRA-only or residual-control baseline on validation loss across at least two seeds.
- Stop condition: Stop if TernRes-LoRA fails to recover at least 25% of ternary degradation on the first two seeds or if adapter cost erases any plausible storage/inference advantage.

## Evidence references

- Artifact root: `<local-path>/projects/ternres-lora-ternary-weights-with-lora-style-residual-adapters-7465077d0b01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
