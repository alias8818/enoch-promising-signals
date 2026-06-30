# Counterexample-Triggered Self-Revision Policy for CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-triggered-self-revision-policy-for-cpu-agents-0101e2a244cd`
Run ID: `counterexample-triggered-self-revision-policy-for-cpu-agents-0101e2a244cd-20260619T230738574062+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d95f05653d68

## What looked useful

Across seeds 0-9, counterexample_gated_revision achieved 1.000 final train and 1.000 holdout success, fixed_no_revision stayed at 0.600 train and 0.500 holdout, and naive_domain_revision fell to 0.400 train and 0.500 holdout after overbroad domain revisions.

## Boundaries and scale limits

20 train and 8 holdout synthetic incidents; no LLM-in-the-loop reasoning, noisy retrieval, real operator traces, or long-horizon production replay. Evidence isolates the policy-update mechanism only.

## Claim scope

In a deterministic synthetic replay with cleanly labeled counterexample cues, cue-scoped counterexample-triggered revision improved train and holdout success versus a fixed policy and avoided the normal-case regressions caused by naive domain-wide revision.

## Why it stopped

No-paper closure: this run produced a small synthetic mechanism signal, not direct publication-grade evidence.

## Recommended next action

Run a bounded LLM-in-the-loop replay using real or realistic CPU-agent traces with noisy counterexample extraction and the same fixed, naive, and gated policy controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop replay for counterexample-triggered CPU-agent policy revision
- Success threshold: Gated revision improves holdout success by at least 15 percentage points over fixed_no_revision and reduces normal-case regressions by at least 50 percent versus naive_domain_revision.
- Stop condition: Stop if gated revision fails to beat fixed_no_revision on holdout or shows regression rates within 10 percent of naive_domain_revision.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-triggered-self-revision-policy-for-cpu-agents-0101e2a244cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
