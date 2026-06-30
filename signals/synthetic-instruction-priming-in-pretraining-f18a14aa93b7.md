# Synthetic Instruction Priming in Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `synthetic-instruction-priming-in-pretraining-f18a14aa93b7`
Run ID: `synthetic-instruction-priming-in-pretraining-f18a14aa93b7-20260526T092541099118+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/026a37900b96

## What looked useful

Instruction-primed runs achieved 235/360 exact held-out matches (65.28%) while matched plain-format and no-task controls achieved 0/360, indicating a format-conditioned prompt-priming mechanism in the tested synthetic setting.

## Boundaries and scale limits

Toy alphabetic tasks only; 2-layer 128-hidden character model; 3 seeds; 4,000 optimizer steps; no natural data, subword tokenization, paraphrase robustness, unseen task families, SFT interaction, or GPT-2-class/large-model validation.

## Claim scope

In a tiny character-level causal transformer trained only on synthetic examples, instruction-formatted pretraining records improved exact greedy execution of held-out prompts using the same Instruction/Input/Answer template versus matched non-instruction records and no-task text.

## Why it stopped

No-paper closure: the local evidence supports a useful toy mechanism signal, but it is template-dependent synthetic evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with paraphrased instruction templates, held-out task families, and a corrupted-label instruction-format control before considering larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paraphrase and Corrupted-Control Test for Synthetic Instruction Priming
- Success threshold: Instruction-primed model improves exact match by at least 20 percentage points over all controls on paraphrased prompts and by at least 10 percentage points on held-out task families.
- Stop condition: Stop if the instruction-primed advantage disappears under paraphrased templates or does not beat the corrupted-label control, indicating template or label memorization rather than robust instruction priming.

## Evidence references

- Artifact root: `<local-path>/projects/synthetic-instruction-priming-in-pretraining-f18a14aa93b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
