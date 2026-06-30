# LoRA on frozen GPT-2-small for tiny domain adaptation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lora-on-frozen-gpt-2-small-for-tiny-domain-adaptation-e48db9390c3a`
Run ID: `lora-on-frozen-gpt-2-small-for-tiny-domain-adaptation-e48db9390c3a-20260619T100401481078+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5bf2564d8304

## What looked useful

LoRA trained 811,008 parameters and improved unseen-entity validation loss from 5.475 to 4.763; full fine-tuning improved it further to 4.357 with all 124,439,808 parameters trainable.

## Boundaries and scale limits

Single synthetic corpus, one seed, GPT-2-small only, short run, no real-domain dataset, no generation/fact-recall evaluation, no rank or hyperparameter ablation.

## Claim scope

On a deterministic synthetic tiny-domain corpus, LoRA rank 8 on frozen GPT-2-small reduced held-out causal language-modeling loss versus the frozen base while training about 0.65% of parameters; full fine-tuning remained stronger.

## Why it stopped

The local synthetic experiment supports the mechanism but is not direct real-world or robust enough for a paper claim.

## Recommended next action

Run a bounded deepen follow-up on a real small-domain corpus with repeated seeds, rank/step ablation, and exact-match fact-recall evaluation; stop this run as useful no-paper evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tiny-domain LoRA adaptation with rank and recall ablations
- Success threshold: LoRA achieves at least 70% of the full-fine-tune loss reduction versus the frozen base and improves held-out fact-recall exact match by at least 20 percentage points while training under 2% of parameters.
- Stop condition: Stop if LoRA fails to improve validation loss over the frozen base in two seeds or reaches less than 30% of the full-fine-tune loss reduction after a reasonable rank/step sweep.

## Evidence references

- Artifact root: `<local-path>/projects/lora-on-frozen-gpt-2-small-for-tiny-domain-adaptation-e48db9390c3a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
