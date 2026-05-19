# End-to-End Causal Tail-Mass Landmark Pooling Without Stabilization

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `end-to-end-causal-tail-mass-landmark-pooling-without-stabi-bfc557c959`
Run ID: `end-to-end-causal-tail-mass-landmark-pooling-without-stabi-bfc557c959-20260517T030423045575+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: End-to-End Causal Tail-Mass Landmark Pooling Without Stabilization: internal_generated:end-to-end-causal-tail-mass-landmark-pooling-without-stabi-bfc557c959

## What looked useful

Tail-landmark pooling reached mean validation loss 2.1275 versus dense 2.1517 and uniform-landmark 2.1359 across seeds 0, 1, and 2. Tail-landmark won 3/3 seeds against dense and 3/3 against the uniform-landmark ablation, but the tail-specific margin over uniform was small.

## Boundaries and scale limits

Evidence is limited to a small character-level corpus, short 128-token contexts, 600-step runs, and an unoptimized reference implementation. It does not establish GPT-2-small-class performance, long-context downstream gains, broad corpus robustness, or practical speed/memory advantages.

## Claim scope

On a 826k-parameter Tiny Shakespeare character-level language-model benchmark with 3 fixed seeds and 600 training steps, causal tail-mass landmark pooling trained end-to-end without extra stabilization and improved validation loss over both a dense causal Transformer baseline and a uniform-landmark control.

## Why it stopped

Bounded validation supports stable small-scale training and a small validation-loss improvement, but it falls short of publication-grade replication and robustness because it lacks GPT-2-small-class baselines, larger corpora, long-context tasks, optimized efficiency evidence, and broader dataset coverage.

## Recommended next action

Stop this branch as no-paper useful evidence: the mechanism signal is reproducible locally, but the controller requested Tier 4 paper-readiness and this follow-up is already at depth 4, so no further follow-up is recommended from this campaign.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-causal-tail-mass-landmark-pooling-without-stabi-bfc557c959`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
