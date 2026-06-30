# Home Fine-Tuning: Ternary GPT-2 Base with Channel-Residual LoRA Adapters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-fine-tuning-ternary-gpt-2-base-with-channel-residual-lora-adapters-ddeb4c9b3c56`
Run ID: `home-fine-tuning-ternary-gpt-2-base-with-channel-residual-lora-adapters-ddeb4c9b3c56-20260613T182841530219+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/faf8d73e53c5

## What looked useful

The channel residual mostly recovers missing per-output-channel scale information. It is useful for global-scale ternary bases and redundant for per-channel ternary bases, making the broad architecture claim implementation-dependent rather than generally supported.

## Boundaries and scale limits

This run did not load or fine-tune GPT-2, did not use real language-modeling data, did not measure perplexity, and did not test optimizer dynamics. Evidence is limited to NumPy projection-repair proxies with synthetic correlated activations.

## Claim scope

On synthetic GPT-2-base-sized 768x768 projection repair, channel-residual LoRA improves frozen global-scale ternary weights by about 28.5-31.7% relative MSE over plain LoRA at ranks 4-32, but provides no meaningful improvement when ternary weights already use per-channel scaling.

## Why it stopped

Closed as no-paper useful-signal proxy evidence: the mechanism is supported only for global-scale ternary repair and is effectively falsified as an added benefit over per-channel ternary plus plain LoRA; full GPT-2 validation remains untested.

## Recommended next action

Run a bounded real GPT-2-small language-model fine-tune comparing dense LoRA, global-scale ternary plus plain LoRA, global-scale ternary plus channel-residual LoRA, per-channel ternary plus plain LoRA, and per-channel ternary plus channel-residual LoRA under equal trainable parameter budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GPT-2-small fine-tune for ternary channel-residual LoRA
- Success threshold: Channel-residual LoRA must reduce validation perplexity by at least 2% versus plain LoRA for global-scale ternary while showing no claimed advantage for per-channel ternary unless it beats plain LoRA by at least 1% under equal trainable parameters.
- Stop condition: Stop if per-channel ternary plus channel-residual LoRA fails to beat per-channel ternary plus plain LoRA by 1% validation perplexity improvement, or if global-scale ternary plus channel-residual LoRA does not beat global-scale ternary plus plain LoRA by 2%.

## Evidence references

- Artifact root: `<local-path>/projects/home-fine-tuning-ternary-gpt-2-base-with-channel-residual-lora-adapters-ddeb4c9b3c56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
