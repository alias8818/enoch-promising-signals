# Profiler-matched text retrieval length curriculum

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `63`
Project ID: `profiler-matched-text-retrieval-length-curriculum-c00fda505f`
Run ID: `profiler-matched-text-retrieval-length-curriculum-c00fda505f-20260517T004953341358+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `63`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Profiler-matched text retrieval length curriculum: internal_generated:profiler-matched-text-retrieval-length-curriculum-c00fda505f

## What looked useful

Short-to-long improved mean uniform retrieval accuracy by only +0.02292 versus constant, improved 3 of 5 seeds, reduced late-position accuracy by -0.02500 with 4 of 5 seeds worse, and was beaten by the long-to-short control on uniform loss. Profiler-matched length schedules affect retrieval behavior, but the observed effect is mixed and not a robust short-to-long mechanism win.

## Boundaries and scale limits

Not validated at GPT-2 small 124M parameters, 1024-token or longer context, natural-language QA/document retrieval, larger value spaces, more key-value pairs per context, long-horizon convergence, or broad optimizer and schedule sweeps.

## Claim scope

In a bounded direct retrieval experiment with a 16.169M parameter GPT-2-style decoder, Wikitext-2/GPT-2 distractor text, randomized key-value bindings, 512-token final evaluation, five paired seeds, and empirically profiler-matched training time, a 128->256->512 short-to-long curriculum did not robustly improve exact retrieval versus constant 512-token training or a 512->256->128 long-to-short ordering control.

## Why it stopped

Tier 3 bounded direct validation failed the success threshold: short-to-long did not reach a 5 percentage point uniform accuracy gain, improved only 3 of 5 paired seeds, worsened late-position retrieval, and did not beat the long-to-short control on loss.

## Recommended next action

Stop this follow-up as a bounded direct negative/mixed result; do not write a paper on the profiler-matched short-to-long retrieval curriculum without a new mechanism that preserves late-position retrieval and beats the long-to-short control.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/profiler-matched-text-retrieval-length-curriculum-c00fda505f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
