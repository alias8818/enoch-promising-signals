# Self-Tree Decoding Without Draft Model on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `self-tree-decoding-without-draft-model-on-gb10-7a571529440f`
Run ID: `self-tree-decoding-without-draft-model-on-gb10-7a571529440f-20260609T075345271356+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/84b358ff9516

## What looked useful

Self-tree expansion generated the same greedy path but slowed decode: baseline 0.1029s for 512 tokens, branch2/depth2 0.1771s, branch2/depth4 0.2517s, branch4/depth4 2.6405s. Candidate positions per output token rose from 1.0 to 3.0, 7.5, and 85.0 respectively.

## Boundaries and scale limits

Tested one small real causal LM, 8 prompts, 64 generated tokens per prompt, fp16, greedy decoding only. Did not test 7B+ models, custom fused tree kernels, sampling acceptance, or production multi-user serving.

## Claim scope

On GB10 with Hugging Face cached greedy decoding for distilgpt2, same-target top-k self-tree expansion without a draft model is slower than serial cached decoding because it evaluates discarded target-model branches while preserving the same number of sequential decode stages.

## Why it stopped

Proxy/early falsification rather than full validation: the direct small-model GB10 test shows the core no-draft mechanism is slower because candidate branch work dominates.

## Recommended next action

Stop this no-draft greedy self-tree line unless a new mechanism reduces target-model branch work; any overturning attempt should first show same-quality speedup with custom kernels or sampling-specific acceptance on a bounded model.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/self-tree-decoding-without-draft-model-on-gb10-7a571529440f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
